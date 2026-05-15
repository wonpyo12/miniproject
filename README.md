## 미니 프로젝트
- ros2를 이용한 자율주행 시뮬레이션
- git clone으로 ros2공식 홈페이지에서 샘플 코드 다운로드
- turtlebot3_gazebo 파일에 turtlebot3_autorace_2020.launch.py파일 사용
- turtlebot3_autorace_2020.world 파일 사용
- node 폴더 추가 
- 신호등 정지,출발 제어를 위해 node 폴더에 traffic_control.py추가

## 기본 설정
- 로봇의 속도,센서 데이터를 주고 받기 위해 시스템 설치 : sudo install ros-humble-turtlebot3-msgs
- 키보드입력으로 로봇 조종 태스트를 위해 설치 : sudo install ros-humble-turtlebot3-teleop
- 환경설정 : source install/setup.bash
- 모델지정 : export TURTLEBOT3_MODEL=waffle_pi
- 빌드 : colcon build --symlink-install

## 3주차 변경사항
- ros2 토픽을 이용하여 파이썬 코드를 이용해 Gazebo환경에서 객체 상태를 변경할려고 하였으나 불가능하다고 판단하여 객체(신호등)를 인식하여 아두이노에서 상태가 변경되면 그 변경된 사항을 통신하여 그 상황에 맞게 동작하도록 변경

- 기존 sample코드에서 turtlebot3_autorace_2020.world파일은 자율주행 수행하기에는 부적합한 부분이 있어 장애물 삭제 및 라인 연결하여 world파일 수정

- 기존 사용하던 모델인 waffle_pi모델이 현재 world파일에 있는 트랙(라인)부분과 맞지 않아 모델 burger로 변경


