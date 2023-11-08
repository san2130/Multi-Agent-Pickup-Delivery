#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16,String,Bool

def sendmsg(bot,val):
    rospy.sleep(2)
    if bot==4:
          print("Bot4 package dropped")
          drop_pub4.publish(val)
          traj_pub4.publish(True)
    else:
          print("Bot2 package dropped")
          drop_pub2.publish(val)
          traj_pub2.publish(True)

def drop4(data):
   sendmsg(4,1)

def drop2(data):
   sendmsg(2,1)

if __name__ == "__main__":
    rospy.init_node('replying', anonymous=True)
    drop_pub4=rospy.Publisher('/dot4/dropdone',Int16,queue_size=0,latch=True)
    drop_pub2=rospy.Publisher('/dot2/dropdone',Int16,queue_size=0,latch=True)
    traj_pub4=rospy.Publisher("/dot4/trajectory_finished", Bool, queue_size=0,latch=True)
    traj_pub2=rospy.Publisher("/dot2/trajectory_finished", Bool, queue_size=0,latch=True)
    rospy.Subscriber("/dot4/drop", String, drop4)
    rospy.Subscriber("/dot2/drop", String, drop2)
    rospy.spin()
