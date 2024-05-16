# urdf2dh
URDF$B%U%!%$%k$GDj5A$5$l$?%^%K%T%e%l!<%?$+$i(BDH$B%Q%i%a!<%?$rCj=P$9$k5!G=$r<BAu$7$F$$$^$9!#(B  

> __Note__  
> `2021.6.1` : $BD>Ns%j%s%/%m%\%C%H$rA[Dj$7$?5!G=$K8BDj$7$F$*$j!"JBNs%j%s%/%m%\%C%H$OA[Dj$7$F$$$^$;$s!#(B


# Features
* URDF$B%U%!%$%k$+$i(BDH$B%Q%i%a!<%?$r7W;;(B
* URDF$B%U%!%$%k$+$i(BDH$B%Q%i%a!<%?$r4pK\$H$7$?F1<!JQ499TNs$r@8@.(B


# How to use
## URDF$B$+$i(BDH$B%Q%i%a!<%?$r7W;;$9$k(B
DH$B%Q%i%a!<%?$rCN$j$?$$(BURDF$B%U%!%$%k(B`example.urdf`$B$rMQ0U$7(B`from_urdf("exmaple.urdf")`$B$r<B9T$9$k$3$H$G(BDH$B%Q%i%a!<%?$,7W;;$5$l$^$9!#(B  
DH$B%Q%i%a!<%?$O(BDict in List$B$G=PNO$5$l$^$9!#%j%9%H$ND9$5$O4X@a$N?t$H0lCW$7$^$9!#(B
```python
from urdf2dh import from_urdf
dhparams = from_urdf("exmaple.urdf")
>>> [
    {"name": "joint1", "a": 0.12, "alpha": 1.507, "d": 0.340, "theta_offset":  1.517},
    {"name": "joint2", "a": 1.87, "alpha":   0.0, "d": 0.000, "theta_offset":    0.0},
    ...,
    {"name": "jointN-1", "a": 0.00, "alpha": 0.750, "d": 0.980, "theta_offset": -1.507},
]
```
`"name"`$B%-!<$NCM$O(BURDF$B$GDj5A$5$l$F$$$k(Bjoint$B$N(Bname$BB0@-$K$J$j$^$9!#(B  
`"a"`$B$H(B`"d"`$B$NC10L$O(B`[mm]`$B$G$9!#(BURDF$B$G$OD9$5$NC10L$,(B`[m]`$B$GI=<($5$l$F$$$k$N$GCm0U$7$F$/$@$5$$!#(B  
`"alpha"`$B!"(B`"theta_offset"`$B$NC10L$O(B`[rad]`$B$H$7$F$$$^$9!#(B


## Example
$B$3$3$G$ONc$H$7$F(Bmycobot$B$N(BURDF$B%U%!%$%k(B [mycobot_urdf.urdf](https://github.com/elephantrobotics/mycobot_ros/blob/main/urdf/mycobot_urdf.urdf) $B$+$i(BDH$B%Q%i%a!<%?$r7W;;$7$^$9!#(B

mycobot$B$N(BDH$B%Q%i%a!<%?$O2<I=$N$h$&$K$J$j$^$9!#(B  
> __mycobot$B$N3F:BI8<4$H(BDH$B%Q%i%a!<%?(B__  
> [https://www.elephantrobotics.com/docs/myCobot-en/2-preparation/2-mycobot_hardware/2-mycobot_hardware.html](https://www.elephantrobotics.com/docs/myCobot-en/2-preparation/2-mycobot_hardware/2-mycobot_hardware.html)

| Joint | alpha[rad] | a[mm] | d[mm]    | theta   | offset[rad] |
|:-----:|:----------:|:-----:|:--------:|:-------:|:-----------:|
| 1     | 0          | 0     | 131.56   | theta_1 | 0           |
| 2     | PI/2       | 0     | 0        | theta_2 | -PI/2       |
| 3     | 0          | -110.4| 0        | theta_3 | 0           |
| 4     | 0          | -96   | 66.39    | theta_4 | -PI/2       |
| 5     | PI/2       | 0     | 73.18    | theta_5 | PI/2        |
| 6     | -PI/2      | 0     | 43.6     | theta_6 | 0           |

mycobot$B$N(BURDF$B%U%!%$%k$O2<5-$N$h$&$K$J$j$^$9!#(B
<details>
<summary>mycobot_urdf.urdf</summary>

```xml
<?xml version="1.0"?>
<robot  xmlns:xacro="http://www.ros.org/wiki/xacro" name="firefighter" >	
<xacro:property name="width" value=".2" />

  <link name="joint1">
    <visual>
      <geometry>
	     <!--- 0.0 0 -0.04  1.5708 3.14159-->
       <mesh filename="package://mycobot_ros/urdf/joint1.dae"/>
      </geometry>
    <origin xyz = "0.0 0 0 " rpy = " 0 0 -1.5708"/>
    </visual>
  </link>

  <link name="joint2">
    <visual>
      <geometry>
       <mesh filename="package://mycobot_ros/urdf/joint2.dae"/>
      </geometry>
    <origin xyz = "0.0 0 -0.06096 " rpy = " 0 0 -1.5708"/>
    </visual>
  </link>

  <link name="joint3">
    <visual>
      <geometry>
       
       <mesh filename="package://mycobot_ros/urdf/joint3.dae"/>
      </geometry>
    <origin xyz = "0.0 0 0.03256 " rpy = " 0 -1.5708 0"/>
    </visual>
  </link>

  <link name="joint4">
    <visual>
      <geometry>
       <!--- 0.0 0 -0.04 -->
       <mesh filename="package://mycobot_ros/urdf/joint4.dae"/>
      </geometry>
    <origin xyz = "0.0 0 0.03056 " rpy = " 0 -1.5708 0"/>
    </visual>
  </link>

<link name="joint5">
    <visual>
      <geometry>
       <!--- 0.0 0 -0.04 -->
       <mesh filename="package://mycobot_ros/urdf/joint5.dae"/>
      </geometry>
    <origin xyz = "0.0 0 -0.03356 " rpy = " 0 -1.5708 1.5708"/>
    </visual>
  </link>

  <link name="joint6">
    <visual>
      <geometry>
       <!--- 0.0 0 -0.04 -->
       <mesh filename="package://mycobot_ros/urdf/joint6.dae"/>
      </geometry>
    <origin xyz = "0 0.00 -0.038 " rpy = " 0 0 0"/>
    </visual>
  </link>

  <link name="joint6_flange">
    <visual>
      <geometry>
       <!--- 0.0 0 -0.04 -->
       <mesh filename="package://mycobot_ros/urdf/joint7.dae"/>
      </geometry>
    <origin xyz = "0.0 0 -0.012 " rpy = " 0 0 0"/>
    </visual>
  </link>

  <joint name="joint2_to_joint1" type="revolute">
    <axis xyz="0 0 1"/>
    <limit effort = "1000.0" lower = "-3.14" upper = "3.14159" velocity = "0"/>
    <parent link="joint1"/>
    <child link="joint2"/>
    <origin xyz= "0 0 0.13156" rpy = "0 0 0"/>  
  </joint>

  <joint name="joint3_to_joint2" type="revolute">
    <axis xyz="0 0 1"/>
    <limit effort = "1000.0" lower = "-3.14" upper = "3.14159" velocity = "0"/>
    <parent link="joint2"/>
    <child link="joint3"/>
    <origin xyz= "0 0  0" rpy = "0 1.5708 -1.5708"/>  
  </joint>


  <joint name="joint4_to_joint3" type="revolute">
    <axis xyz=" 0 0 1"/>
    <limit effort = "1000.0" lower = "-3.14" upper = "3.14159" velocity = "0"/>
    <parent link="joint3"/>
    <child link="joint4"/>
    <origin xyz= "  -0.1104 0 0   " rpy = "0 0 0"/>  
  </joint>

  <joint name="joint5_to_joint4" type="revolute">
    <axis xyz=" 0 0 1"/>
    <limit effort = "1000.0" lower = "-3.14" upper = "3.14159" velocity = "0"/>
    <parent link="joint4"/>
    <child link="joint5"/>
    <origin xyz= "-0.096 0 0.06462" rpy = "0 0 -1.5708"/>  
  </joint>

  <joint name="joint6_to_joint5" type="revolute">
    <axis xyz="0 0 1"/>
    <limit effort = "1000.0" lower = "-3.14" upper = "3.14159" velocity = "0"/>
    <parent link="joint5"/>
    <child link="joint6"/>
    <origin xyz= "0 -0.07318 0" rpy = "1.5708 -1.5708 0"/>  
  </joint>

  <joint name="joint6output_to_joint6" type="revolute">
    <axis xyz="0 0 1"/>
    <limit effort = "1000.0" lower = "-3.14" upper = "3.14159" velocity = "0"/>
    <parent link="joint6"/>
    <child link="joint6_flange"/>
    <origin xyz= "0 0.0456 0" rpy = "-1.5708 0 0"/>  
  </joint>
</robot>
```
</details>

$B<B9T$9$k(BPython$B%9%/%j%W%H$r(B`example.py`$B$H$7!"<!$N$h$&$J%U%)%k%@9=@.$rA[Dj$7$F$$$^$9!#(B
```bash
./urdf2dh_example
    $B(!(B example.py
    $B(!(B mycobot_urdf.urdf
```

example.py$B$NFbMF$H!"$=$N<B9T7k2L$,<!$N$h$&$K$J$j$^$9!#(B
```python
from urdf2dh import from_urdf
print(from_urdf("mycobot_urdf.urdf"))
>>> [
    {"name": "joint2_to_joint1", "a":0,     "alpha": 0,      "d": 131.56,   "theta_offset": 0},
    {"name": "joint3_to_joint2", "a":0,     "alpha": 1.5707, "d": 0,        "theta_offset": -1.5707},
    {"name": "joint4_to_joint3", "a":-110.4,"alpha": 0,      "d": 0,        "theta_offset": 0},
    {"name": "joint5_to_joint4", "a":-96,   "alpha": 0,      "d": 66.39,    "theta_offset": -1.5707},
    {"name": "joint6_to_joint5", "a":0,     "alpha": 1.5707, "d": 73.18,    "theta_offset": 1.5707},
    {"name": "joint6output_to_joint6", "a":0,     "alpha": -1.5707,"d": 43.6,     "theta_offset": 0},
]
```

