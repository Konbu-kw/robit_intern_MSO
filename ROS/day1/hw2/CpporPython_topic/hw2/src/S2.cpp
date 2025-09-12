#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "std_msgs/msg/int32.hpp"
#include "std_msgs/msg/float32.hpp"

using std::placeholders::_1;

class Subscriber1 : public rclcpp::Node
{
  public:
    Subscriber1()
    : Node("Cpp_SUB2")
    {
      string_subscription_ = this->create_subscription<std_msgs::msg::String>("cpps", 10, std::bind(&Subscriber1::string_callback, this, _1));
      int_subscription_ = this->create_subscription<std_msgs::msg::Int32>("cppi", 10, std::bind(&Subscriber1::int_callback,this,_1));
      float_subscription_ = this->create_subscription<std_msgs::msg::Float32>("cppf", 10, std::bind(&Subscriber1::float_callback, this, _1));
    }

  private:
    void string_callback(const std_msgs::msg::String & msg) const
    {
      RCLCPP_INFO(this->get_logger(), "From_CppS: '%s'", msg.data.c_str());
    }
    void int_callback(const std_msgs::msg::Int32 & msg) const
    {
      RCLCPP_INFO(this->get_logger(), "From_CppI: '%d'", msg.data);
    }
    void float_callback(const std_msgs::msg::Float32 & msg) const
    {
      RCLCPP_INFO(this->get_logger(), "From_CppF: '%f'", msg.data);
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr string_subscription_;
    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr int_subscription_;
    rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr float_subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<Subscriber1>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}