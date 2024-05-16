# urdf2dh
URDFファイルで定義されたマニピュレータからDHパラメータを抽出する機能を実装しています。  

> __Note__  
> `2021.6.1` : 直列リンクロボットを想定した機能に限定しており、並列リンクロボットは想定していません。


# Features
* URDFファイルからDHパラメータを計算
* URDFファイルからDHパラメータを基本とした同次変換行列を生成


# How to use
## URDFからDHパラメータを計算する
DHパラメータを知りたいURDFファイル`example.urdf`を用意し`from_urdf("exmaple.urdf")`を実行することでDHパラメータが計算されます。  
DHパラメータはDict in Listで出力されます。リストの長さは関節の数と一致します。
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
`"name"`キーの値はURDFで定義されているjointのname属性になります。  
`"a"`と`"d"`の単位は`[mm]`です。URDFでは長さの単位が`[m]`で表示されているので注意してください。  
`"alpha"`、`"theta_offset"`の単位は`[rad]`としています。


## Example
ここでは例としてmycobotのURDFファイル [mycobot_urdf.urdf](https://github.com/elephantrobotics/mycobot_ros/blob/main/urdf/mycobot_urdf.urdf) からDHパラメータを計算します。

mycobotのDHパラメータは下表のようになります。  
> __mycobotの各座標軸とDHパラメータ__  
> [https://www.elephantrobotics.com/docs/myCobot-en/2-preparation/2-mycobot_hardware/2-mycobot_hardware.html](https://www.elephantrobotics.com/docs/myCobot-en/2-preparation/2-mycobot_hardware/2-mycobot_hardware.html)

| Joint | alpha[rad] | a[mm] | d[mm]    | theta   | offset[rad] |
|:-----:|:----------:|:-----:|:--------:|:-------:|:-----------:|
| 1     | 0          | 0     | 131.56   | theta_1 | 0           |
| 2     | PI/2       | 0     | 0        | theta_2 | -PI/2       |
| 3     | 0          | -110.4| 0        | theta_3 | 0           |
| 4     | 0          | -96   | 66.39    | theta_4 | -PI/2       |
| 5     | PI/2       | 0     | 73.18    | theta_5 | PI/2        |
| 6     | -PI/2      | 0     | 43.6     | theta_6 | 0           |

mycobotのURDFファイルは下記のようになります。
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

実行するPythonスクリプトを`example.py`とし、次のようなフォルダ構成を想定しています。
```bash
./urdf2dh_example
    ─ example.py
    ─ mycobot_urdf.urdf
```

example.pyの内容と、その実行結果が次のようになります。
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

