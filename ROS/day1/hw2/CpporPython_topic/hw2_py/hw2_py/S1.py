import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32, Float32

class PY_SUB(Node):
    def __init__(self):
        super().__init__('PY_SUB')
        self.string_subscriber = self.create_subscription(String, 'cpps', self.string_message, 10)
        self.int_subscriber = self.create_subscription(Int32, 'cppi', self.int_message, 10)
        self.float_subscriber = self.create_subscription(Float32, 'cppf', self.float_message, 10)
    
    def string_message(self,msg):
        self.get_logger().info('{0}'.format(msg.data))
    def int_message(self, msg):
        self.get_logger().info('{0}'.format(msg.data))
    def float_message(self, msg):
        self.get_logger().info('{0}'.format(msg.data))

def main(args=None):
    rclpy.init(args=args)
    node = PY_SUB()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (Ctrl C)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()