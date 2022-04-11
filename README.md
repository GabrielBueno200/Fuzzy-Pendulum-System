# Fuzzy-Logic-System




<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/WebisD/Fuzzy-Logic-System">

  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/WebisD/Fuzzy-Logic-System">
  
  <a href="https://github.com/henriquevital00/pong-game/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/WebisD/Fuzzy-Logic-System">
  </a>
  
   <img alt="GitHub" src="https://img.shields.io/github/license/WebisD/Fuzzy-Logic-System">
</p>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/antuniooh/Relic">
    <img src="https://www.researchgate.net/profile/Mariagrazia-Dotoli/publication/268276446/figure/fig1/AS:619977862287362@1524825649487/Pendulum-swing-up-and-stabilization-zone_Q640.jpg" alt="Logo" width="450">
  </a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#-how-to-run">How To Run</a>
    </li>
    <li>
      <a href="#-authors">Authors</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 💻 About The Project
Semiannual project of the subject of Artificial Intelligence and Robotics, taught at Centro Universitário FEI. It consists of a fuzzy logic system in python for the balance of a pendulum.

The article <a href="https://www.researchgate.net/publication/228633624_Fuzzy_Control_of_a_Real_Time_Inverted_Pendulum_System">Fuzzy Control of a Real Time Inverted Pendulum System</a> (KIZIR, Selçuk; BINGUL; Zafer; OYZUL, Cuneyt) concepts were used to the algorithm development.

## Swing Up

### Input parameters
Two parameters were used: pendulum angle and angular velocity. The membership functions below were applied:

![image](https://user-images.githubusercontent.com/56837996/162648090-97ce0c8a-d204-4001-a204-60ba0c763341.png)

### Rules
![image](https://user-images.githubusercontent.com/56837996/162648530-446c8ffe-8cac-44c7-92e7-45b0ba8b960c.png)

## Stabilization

### Input parameters
Four parameters were used: pendulum angle, angular velocity, cart position, cart velocity. The membership functions below were applied:

![image](https://user-images.githubusercontent.com/56837996/162648332-01a942b8-d3bb-469b-b82a-ffae6799901e.png)

### Rules
![image](https://user-images.githubusercontent.com/56837996/162648486-7600f918-2af6-4531-9da2-87bd65e08445.png)

## Output
The system output is the pendulum applied force. Swing-up and stabilization rules use the same output fuzzy subsets.

The output membership function is in the figure below

![image](https://user-images.githubusercontent.com/56837996/162648788-26811ee5-a890-4818-b9a6-18cf49fdd759.png)

<!-- HOW TO RUN -->
## 🚀 How To Run

### Terminal
```bash

# Clone the repository
$ git clone https://github.com/WebisD/Arkanoid_Cpp.git

# Access the project folder in your terminal / cmd
$ cd Arkanoid_Cpp
# Open in Visual Studio 

```

## 🤖 Authors

 [Gabriel Bueno](https://github.com/GabrielBueno200)|  [Weverson da Silva](https://github.com/WebisD)
:-------------------------:|:-------------------------:|
 <img src="https://avatars.githubusercontent.com/u/56837996?v=4" alt="drawing" width="150"/>  | <img src="https://avatars.githubusercontent.com/u/49571908?v=4" alt="drawing" width="150"/>
22.119.077-0 | 22.119.004-4
