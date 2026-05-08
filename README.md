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