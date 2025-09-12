import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32, Float32

class py_string(Node):
    def __init__(self):
        super().__init__('PY_PUB')
        self.string_publisher = self.create_publisher(String, 'pys', 10)
        self.int_publisher = self.create_publisher(Int32, 'pyi', 10)
        self.float_publisher = self.create_publisher(Float32, 'pyf',10)
        self.timer = self.create_timer(1, self.publish_string_msg)
        self.count = 0

    def publish_string_msg(self):
        msg_s = String()
        msg_s.data = 'From_PY'
        
        msg_i = Int32()
        msg_i.data = self.count

        msg_f = Float32()
        msg_f.data = 2.414

        self.string_publisher.publish(msg_s)
        self.int_publisher.publish(msg_i)
        self.float_publisher.publish(msg_f)
        self.get_logger().info('{0}'.format(msg_s.data))
        self.get_logger().info('{0}'.format(msg_i.data))
        self.get_logger().info('{0}'.format(msg_f.data))
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = py_string()
    try:
        rclpy.spin(node)
    except:
        node.get_logger().info('Keyboard Interrupt (Ctrl C)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
