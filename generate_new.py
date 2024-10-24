# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:28:26 2024

@author: herzogag
"""

import pyrosim.pyrosim as ps

# Global parameters
l = 1 # length
w = 1 # width 
h = 1 # height 

x = 0
y = 0
z = 1

    
def Create_Robot():
    ps.Start_URDF("body.urdf")
    ps.Send_Cube(name="Torso",pos=[x,y,z],size=[l,w,h]) # Parent
# =============================================================================
#     ps.Send_Joint(name="Right_Torso", parent="Torso", child="Right_Arm", type="revolute", position = [0.5,0,0.5])
#     ps.Send_Cube(name="Right_Arm", pos = [1, 0.5, -0.25], size = [2, 0.5, 0.5])
#     ps.Send_Joint(name = "Left_Torso", parent ="Torso", child="Left_Arm", type ="revolute", position = [-0.5, 0, 0.5])  
#     ps.Send_Cube(name="Left_Arm", pos = [-1, 0.5, -0.25], size = [2, 0.5, 0.5])
# =============================================================================
    ps.Send_Joint(name="Right_Torso", parent="Torso", child="Right_Arm", type="revolute", position = [0.5,0,0.5])
    ps.Send_Cube(name="Right_Arm", pos = [1, 0.5, 0.25], size = [2, 0.5, 0.5])
    ps.Send_Joint(name = "Left_Torso", parent ="Torso", child="Left_Arm", type ="revolute", position = [-0.5, 0, 0.5])  
    ps.Send_Cube(name="Left_Arm", pos = [-1, 0.5, 0.25], size = [2, 0.5, 0.5])
    ps.End()
    
Create_Robot()