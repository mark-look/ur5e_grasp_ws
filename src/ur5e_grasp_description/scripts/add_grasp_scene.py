#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from moveit_msgs.srv import ApplyPlanningScene
from moveit_msgs.msg import PlanningScene, CollisionObject
from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import Pose


class GraspSceneLoader(Node):

    def __init__(self):
        super().__init__('grasp_scene_loader')

        self.client = self.create_client(
            ApplyPlanningScene,
            '/apply_planning_scene'
        )

        self.get_logger().info(
            'Waiting for MoveIt planning scene service...'
        )

        if not self.client.wait_for_service(timeout_sec=10.0):
            self.get_logger().error(
                'ApplyPlanningScene service unavailable!'
            )
            raise RuntimeError('MoveIt service unavailable')

        self.load_scene()

    def create_box(
        self, name, x, y, z, sx, sy, sz
    ):
        obj = CollisionObject()
        obj.header.frame_id = 'world'
        obj.id = name

        primitive = SolidPrimitive()
        primitive.type = SolidPrimitive.BOX
        primitive.dimensions = [sx, sy, sz]

        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        pose.orientation.w = 1.0

        obj.primitives.append(primitive)
        obj.primitive_poses.append(pose)
        obj.operation = CollisionObject.ADD

        return obj

    def create_sphere(self, name, x, y, z, radius):
        obj = CollisionObject()
        obj.header.frame_id = 'world'
        obj.id = name

        primitive = SolidPrimitive()
        primitive.type = SolidPrimitive.SPHERE
        primitive.dimensions = [radius]

        pose = Pose()
        pose.position.x = x
        pose.position.y = y
        pose.position.z = z
        pose.orientation.w = 1.0

        obj.primitives.append(primitive)
        obj.primitive_poses.append(pose)
        obj.operation = CollisionObject.ADD

        return obj

    def load_scene(self):

        scene = PlanningScene()
        scene.is_diff = True

        # 桌面
        scene.world.collision_objects.append(
            self.create_box(
                'table_top',
                0.5, 0.0, 0.40,
                0.36, 0.8, 0.04
            )
        )

        # 四条桌腿
        legs = [
            (0.655, 0.35),
            (0.345, 0.35),
            (0.655, -0.35),
            (0.345, -0.35)
        ]

        for i, (x, y) in enumerate(legs):
            scene.world.collision_objects.append(
                self.create_box(
                    f'table_leg_{i+1}',
                    x, y, 0.19,
                    0.05, 0.05, 0.38
                )
            )

        # 红球
        scene.world.collision_objects.append(
            self.create_sphere(
                'red_ball',
                0.5, 0.0, 0.46,
                0.04
            )
        )

        request = ApplyPlanningScene.Request()
        request.scene = scene

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            if future.result().success:
                self.get_logger().info(
                    'Successfully added table and red ball!'
                )
            else:
                self.get_logger().error(
                    'Failed to apply planning scene!'
                )
        else:
            self.get_logger().error(
                'Service call failed!'

            )


def main():
    rclpy.init()

    node = GraspSceneLoader()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()