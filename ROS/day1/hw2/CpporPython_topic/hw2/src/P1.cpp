#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include "rclcpp/rclcpp.hpp"

#include "std_msgs/msg/string.hpp"
#include "std_msgs/msg/int32.hpp"
#include "std_msgs/msg/float32.hpp"

using namespace std::chrono_literals;

class Publisher1 : public rclcpp::Node
{
  public:
    Publisher1()
    : Node("Cpp_PUB"), count_(0)
    {
      string_publisher_ = this->create_publisher<std_msgs::msg::String>("cpps", 10);
      int_publisher_ = this->create_publisher<std_msgs::msg::Int32>("cppi",10);
      float_publisher_ = this->create_publisher<std_msgs::msg::Float32>("cppf",10);
      timer_ = this->create_wall_timer(1s, std::bind(&Publisher1::timer_callback, this));
    }

  private:
    void timer_callback()
    {
      auto string1 = std_msgs::msg::String();
      string1.data = "From_Cpp";
      RCLCPP_INFO(this->get_logger(), "OUTPUT(S): '%s'", string1.data.c_str());
      string_publisher_->publish(string1);

      auto int1 = std_msgs::msg::Int32();
      int int1data = count_++;
      int1.data = int1data;
      RCLCPP_INFO(this->get_logger(), "OUTPUT(I): '%d'", int1.data);
      int_publisher_->publish(int1);

      auto float1 = std_msgs::msg::Float32();
      float1.data = 3.14f;
      RCLCPP_INFO(this->get_logger(), "OUTPUT(F): '%f'", float1.data);
      float_publisher_ ->publish(float1);
    }
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr string_publisher_;
    rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr int_publisher_;
    rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr float_publisher_;
    size_t count_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<Publisher1>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}