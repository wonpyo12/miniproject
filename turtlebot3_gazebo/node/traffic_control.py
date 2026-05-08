import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32 

class TrafficLightNode(Node):
    def __init__(self):
        super().__init__('traffic_control_node')
        self.publisher_ = self.create_publisher(Int32, '/traffic_light_status', 10)
        self.timer = self.create_timer(5.0, self.timer_callback) # 5초 간격
        self.state = 0 # 0:빨강, 1:노랑, 2:초록

    def timer_callback(self):
        msg = Int32()
        msg.data = self.state
        self.publisher_.publish(msg)
        self.get_logger().info(f'신호 변경: {self.state}')
        self.state = (self.state + 1) % 3

def main():
    rclpy.init()
    node = TrafficLightNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()