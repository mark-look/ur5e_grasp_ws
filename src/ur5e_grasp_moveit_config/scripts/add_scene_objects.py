import rclpy

from rclpy.node import Node

from moveit_msgs.srv import ApplyPlanningScene
from moveit_msgs.msg import PlanningScene, CollisionObject

from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import Pose


class AddSceneObjects(Node):

    def __init__(self):
        super().__init__('add_scene_objects')

        self.client = self.create_client(
            ApplyPlanningScene,
            '/apply_planning_scene'
        )

        self.get_logger().info('Waiting for ApplyPlanningScene service...')

        if not self.client.wait_for_service(timeout_sec=10.0):
            self.get_logger().error('ApplyPlanningScene service unavailable')
            return

        scene = PlanningScene()
        scene.is_diff = True

        # 桌面
        self.add_box(
            scene, 'table_top',
            [0.65, 0.0, 0.40],
            [0.8, 0.8, 0.04]
        )

        # 四根桌腿
        leg_positions = [
            [1.00, 0.35, 0.19],
            [0.30, 0.35, 0.19],
            [1.00, -0.35, 0.19],
            [0.30, -0.35, 0.19]
        ]

        for i, position in enumerate(leg_positions):
            self.add_box(
                scene,
                f'table_leg_{i+1}',
                position,
                [0.05, 0.05, 0.38]
            )

        # 红球
        self.add_sphere(
            scene,
            'red_ball',
            [0.65, 0.0, 0.46],
            0.04
        )

        request = ApplyPlanningScene.Request()
        request.scene = scene

        future = self.client.call_async(request)

        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            if future.result().success:
                self.get_logger().info(
                    'Successfully added 6 collision objects!'
                )
            else:
                self.get_logger().error(
                    'Failed to apply planning scene'
                )
        else:
            self.get_logger().error('Service call failed')

    def add_box(self, scene, object_id, position, dimensions):

        obj = CollisionObject()
        obj.header.frame_id = 'world'
        obj.id = object_id

        primitive = SolidPrimitive()
        primitive.type = SolidPrimitive.BOX
        primitive.dimensions = dimensions

        pose = Pose()
        pose.position.x = position[0]
        pose.position.y = position[1]
        pose.position.z = position[2]
        pose.orientation.w = 1.0

        obj.primitives.append(primitive)
        obj.primitive_poses.append(pose)
        obj.operation = CollisionObject.ADD

        scene.world.collision_objects.append(obj)

    def add_sphere(self, scene, object_id, position, radius):

        obj = CollisionObject()
        obj.header.frame_id = 'world'
        obj.id = object_id

        primitive = SolidPrimitive()
        primitive.type = SolidPrimitive.SPHERE
        primitive.dimensions = [radius]

        pose = Pose()
        pose.position.x = position[0]
        pose.position.y = position[1]
        pose.position.z = position[2]
        pose.orientation.w = 1.0

        obj.primitives.append(primitive)
        obj.primitive_poses.append(pose)
        obj.operation = CollisionObject.ADD

        scene.world.collision_objects.append(obj)


def main(args=None):

    rclpy.init(args=args)

    node = AddSceneObjects()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()