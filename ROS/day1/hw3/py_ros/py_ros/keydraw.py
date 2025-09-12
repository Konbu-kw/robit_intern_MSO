import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
import time

import sys
import termios
import tty

class KeyDraw(Node):
    def __init__(self):
        super().__init__('key_draw')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.set_pen_client = self.create_client(SetPen, '/turtle1/set_pen')


    def publish_twist(self, linear_x=0.0, angular_z=0.0, repeat=0):
        twist = Twist() 
        twist.linear.x = linear_x
        twist.angular.z = angular_z

        for i in range(repeat):
            self.publisher.publish(twist)
            time.sleep(1)

        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)

    def pen(self, r, g, b, width, off=0):
        color = SetPen.Request()
        color.r = r
        color.g = g
        color.b = b
        color.width = width
        color.off = off

        future = self.set_pen_client.call_async(color)
        rclpy.spin_until_future_complete(self, future)

    def draw_triangle(self):
        self.pen(255, 0, 0, 3)
        for i in range(3):
            self.publish_twist(linear_x=2.0, repeat=1)
            self.publish_twist(angular_z=2.0944, repeat=1)

    def draw_square(self):
        self.pen(0, 255, 0, 5)
        for i in range(4):
            self.publish_twist(linear_x=2.0, repeat=1)
            self.publish_twist(angular_z=1.5708, repeat=1)

    def draw_circle1(self):
        self.pen(0, 0, 255, 7)
        self.publish_twist(linear_x=2.0, angular_z=2.0, repeat=4)

    def draw_circle2(self):
        self.pen(255, 255, 255, 9)
        self.publish_twist(linear_x=1.0, angular_z=3.0, repeat=4)

    def keyboard_loop(self):
        print("W: Triangle, S: Square, A: Circle1, D: Circle2")
        while True:
            key = keyboard_input()
            if key == 'w':
                self.draw_triangle()
            elif key == 's':
                self.draw_square()
            elif key == 'a':
                self.draw_circle1()
            elif key == 'd':
                self.draw_circle2()

def main():
    rclpy.init()
    node = KeyDraw()
    try:
        node.keyboard_loop()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (Ctrl C)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

def keyboard_input():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

if __name__ == "__main__":
    main()
