# Resultados

## Entradas utilizadas para os resultados a seguir:

![image](https://user-images.githubusercontent.com/49571908/163293619-01ff7bb3-c3a5-46d0-abff-a41737dbe4bd.png)
![image](https://user-images.githubusercontent.com/49571908/163294851-f6dccced-16eb-44ac-af80-6ab9b3b83d9d.png)


## Função de pertinência para as saídas (força aplicada)

![image](https://user-images.githubusercontent.com/49571908/163292829-e6ae1425-4d77-4d5c-aff3-208f72adaee4.png)


## Swing Up

- Funções de pertinência ângulo
  ```python
  self.angle = Antecedent(np.arange(0, 401, 1), 'angle')

  self.angle['NLS'] = fuzz.trimf(self.angle.universe, [90, 130, 170])
  self.angle['NBS'] = fuzz.trimf(self.angle.universe, [30, 150, 170])
  self.angle['SALN'] = fuzz.trimf(self.angle.universe, [170, 175, 180])
  self.angle['Z'] = fuzz.trimf(self.angle.universe, [180, 180, 180])
  self.angle['SALP'] = fuzz.trimf(self.angle.universe, [180, 185, 190])
  self.angle['PBS'] = fuzz.trimf(self.angle.universe, [190, 210, 330])
  self.angle['PLS'] = fuzz.trimf(self.angle.universe, [190, 230, 270])
  ```
  
  ![image](https://user-images.githubusercontent.com/49571908/163292440-3e3546b2-c5ac-45e9-9178-40fe1fd37cc9.png)

  
 - Funções de pertinência velocidade ângular
   ```python
    self.angular_velocity = Antecedent(np.arange(-10, 11, 0.1), 'angularVelocity')

    self.angular_velocity['NEG'] = fuzz.trapmf(self.angular_velocity.universe, [-10, -10, -1, 0])
    self.angular_velocity['ZS'] = fuzz.trapmf(self.angular_velocity.universe, [-0.1, 0, 0, 0.1])
    self.angular_velocity['POS'] = fuzz.trapmf(self.angular_velocity.universe, [0, 1, 10, 10])
    ```
    
    ![image](https://user-images.githubusercontent.com/49571908/163292477-ccddb074-26e3-4667-ac39-090c8e4c085c.png)

    
  - Regras
    ```python
    self.rules = [
        Rule(self.angle['NLS'] & self.angular_velocity['POS'], self.applied_force['NB']),
        Rule(self.angle['NBS'] & self.angular_velocity['POS'], self.applied_force['Z']),
        Rule(self.angle['SALN'] & self.angular_velocity['POS'], self.applied_force['N']),
        Rule(self.angle['Z'] & self.angular_velocity['ZS'], self.applied_force['P']),
        Rule(self.angle['SALP'] & self.angular_velocity['NEG'], self.applied_force['P']),
        Rule(self.angle['PBS'] & self.angular_velocity['NEG'], self.applied_force['Z']),
        Rule(self.angle['PLS'] & self.angular_velocity['NEG'], self.applied_force['PB'])
    ]
    ```
    
   - Superfície de decisão
   
     ![image](https://user-images.githubusercontent.com/49571908/163293004-56110317-141f-4e30-9b5c-93941cdd7415.png)
     ![image](https://user-images.githubusercontent.com/49571908/163293051-c699610b-b266-458c-a4ba-0d2baf6a4e99.png)
     ![image](https://user-images.githubusercontent.com/49571908/163293077-e4e0e990-2780-415c-9431-3d460826746e.png)

   

  ## Stabilization

- Funções de pertinência ângulo
  ```python
  self.angle = Antecedent(np.arange(-30, 30, 0.5), 'angle')

  self.angle['NVB'] = fuzz.trapmf(self.angle.universe, [-30, -30, -18, -12])
  self.angle['NB'] = fuzz.trimf(self.angle.universe, [-16.5, -10.5, -4.5])
  self.angle['N'] = fuzz.trimf(self.angle.universe, [-9, -4.5, 0])
  self.angle['ZO'] = fuzz.trimf(self.angle.universe, [-3, 0, 3])
  self.angle['P'] = fuzz.trimf(self.angle.universe, [0, 4.5, 9])
  self.angle['PB'] = fuzz.trimf(self.angle.universe, [4.5, 10.5, 16.5])
  self.angle['PVB'] = fuzz.trapmf(self.angle.universe, [12, 18, 30, 30])
  ```
  
  ![image](https://user-images.githubusercontent.com/49571908/163294209-28f8b4d7-3273-4642-a026-d2bf950d5888.png)

  
 - Funções de pertinência velocidade ângular
   ```python
    self.angular_velocity = Antecedent(np.arange(-6, 6, 0.1), 'angularVelocity')

    self.angular_velocity['NB'] = fuzz.trapmf(self.angular_velocity.universe, [-6, -6, -4.2, -1.7])
    self.angular_velocity['N'] = fuzz.trimf(self.angular_velocity.universe, [-3.6, -1.7, 0])
    self.angular_velocity['ZO'] = fuzz.trimf(self.angular_velocity.universe, [-1.7, 0, 1.7])
    self.angular_velocity['P'] = fuzz.trimf(self.angular_velocity.universe, [0, 1.7, 3.6])
    self.angular_velocity['PB'] = fuzz.trapmf(self.angular_velocity.universe, [1.7, 4.2, 6, 6])
    ```
    
    ![image](https://user-images.githubusercontent.com/49571908/163294422-1198920a-f857-4556-a01d-9b102b1a9563.png)

  - Funções de pertinência posição do carrinho 
   
    ```python
    self.cart_position = Antecedent(np.arange(-0.4, 0.4, 0.05), 'cartPosition')

    self.cart_position['NBIG'] = fuzz.trapmf(self.cart_position.universe, [-0.4, -0.4, -0.3, -0.15])
    self.cart_position['NEG'] = fuzz.trimf(self.cart_position.universe, [-0.3, -0.15, 0])
    self.cart_position['Z'] = fuzz.trimf(self.cart_position.universe, [-0.15, 0, 0.15])
    self.cart_position['POS'] = fuzz.trimf(self.cart_position.universe, [0, 0.15, 0.3])
    self.cart_position['PBIG'] = fuzz.trapmf(self.cart_position.universe, [0.15, 0.3, 0.4, 0.4])
    ```
    
    ![image](https://user-images.githubusercontent.com/49571908/163294474-66fa1636-b694-4952-b597-7605b5d478f4.png)
    
  - Funções de pertinência velocidade do carrinho
   
    ```python
    self.cart_velocity = Antecedent(np.arange(-1, 1, 0.1), 'cartVelocity')

    self.cart_velocity['NEG'] = fuzz.trapmf(self.cart_velocity.universe, [-1, -1, -0.1, 0])
    self.cart_velocity['ZERO'] = fuzz.trimf(self.cart_velocity.universe, [-0.1, 0, 0.1])
    self.cart_velocity['POS'] = fuzz.trapmf(self.cart_velocity.universe, [0, 0.1, 1, 1])
    ```
    
    ![image](https://user-images.githubusercontent.com/49571908/163294537-f460365f-ff1d-46d3-9edf-564935593a04.png)
    
  - Regras
    ```python
    self.rules = [
        Rule(self.cart_position['NBIG'] & self.cart_velocity['NEG'], self.applied_force['PVVB']),
        Rule(self.cart_position['NEG'] & self.cart_velocity['NEG'], self.applied_force['PVB']),
        Rule(self.cart_position['Z'] & self.cart_velocity['NEG'], self.applied_force['PB']),
        Rule(self.cart_position['Z'] & self.cart_velocity['ZERO'], self.applied_force['Z']),
        Rule(self.cart_position['Z'] & self.cart_velocity['POS'], self.applied_force['NB']),
        Rule(self.cart_position['POS'] & self.cart_velocity['POS'], self.applied_force['NVB']),
        Rule(self.cart_position['PBIG'] & self.cart_velocity['POS'], self.applied_force['NVVB']),

        Rule(self.angle['NVB'] & self.angular_velocity['NB'], self.applied_force['NVVB']),
        Rule(self.angle['NVB'] & self.angular_velocity['N'], self.applied_force['NVVB']),
        Rule(self.angle['NVB'] & self.angular_velocity['ZO'], self.applied_force['NVB']),
        Rule(self.angle['NVB'] & self.angular_velocity['P'], self.applied_force['NB']),
        Rule(self.angle['NVB'] & self.angular_velocity['PB'], self.applied_force['N']),

        Rule(self.angle['NB'] & self.angular_velocity['NB'], self.applied_force['NVVB']),
        Rule(self.angle['NB'] & self.angular_velocity['N'], self.applied_force['NVB']),
        Rule(self.angle['NB'] & self.angular_velocity['ZO'], self.applied_force['NB']),
        Rule(self.angle['NB'] & self.angular_velocity['P'], self.applied_force['N']),
        Rule(self.angle['NB'] & self.angular_velocity['PB'], self.applied_force['Z']),

        Rule(self.angle['N'] & self.angular_velocity['NB'], self.applied_force['NVB']),
        Rule(self.angle['N'] & self.angular_velocity['N'], self.applied_force['NB']),
        Rule(self.angle['N'] & self.angular_velocity['ZO'], self.applied_force['N']),
        Rule(self.angle['N'] & self.angular_velocity['P'], self.applied_force['Z']),
        Rule(self.angle['N'] & self.angular_velocity['PB'], self.applied_force['P']),

        Rule(self.angle['ZO'] & self.angular_velocity['NB'], self.applied_force['NB']),
        Rule(self.angle['ZO'] & self.angular_velocity['N'], self.applied_force['N']),
        Rule(self.angle['ZO'] & self.angular_velocity['ZO'], self.applied_force['Z']),
        Rule(self.angle['ZO'] & self.angular_velocity['P'], self.applied_force['P']),
        Rule(self.angle['ZO'] & self.angular_velocity['PB'], self.applied_force['PB']),

        Rule(self.angle['P'] & self.angular_velocity['NB'], self.applied_force['N']),
        Rule(self.angle['P'] & self.angular_velocity['N'], self.applied_force['Z']),
        Rule(self.angle['P'] & self.angular_velocity['ZO'], self.applied_force['P']),
        Rule(self.angle['P'] & self.angular_velocity['P'], self.applied_force['PB']),
        Rule(self.angle['P'] & self.angular_velocity['PB'], self.applied_force['PVB']),

        Rule(self.angle['PB'] & self.angular_velocity['NB'], self.applied_force['Z']),
        Rule(self.angle['PB'] & self.angular_velocity['N'], self.applied_force['P']),
        Rule(self.angle['PB'] & self.angular_velocity['ZO'], self.applied_force['PB']),
        Rule(self.angle['PB'] & self.angular_velocity['P'], self.applied_force['PVB']),
        Rule(self.angle['PB'] & self.angular_velocity['PB'], self.applied_force['PVVB']),

        Rule(self.angle['PVB'] & self.angular_velocity['NB'], self.applied_force['P']),
        Rule(self.angle['PVB'] & self.angular_velocity['N'], self.applied_force['PB']),
        Rule(self.angle['PVB'] & self.angular_velocity['ZO'], self.applied_force['PVB']),
        Rule(self.angle['PVB'] & self.angular_velocity['P'], self.applied_force['PVVB']),
        Rule(self.angle['PVB'] & self.angular_velocity['PB'], self.applied_force['PVVB'])
      ]
    ```
    
   - Superfície de decisão
   
     ![image](https://user-images.githubusercontent.com/49571908/163294666-2383e573-c806-44ca-8d48-86340aeab883.png)
     ![image](https://user-images.githubusercontent.com/49571908/163294697-e26c1491-fbf9-40cd-80d8-c82b82520ebc.png)
     ![image](https://user-images.githubusercontent.com/49571908/163294721-7e6ac15f-c0bd-4463-9993-6675342f3a21.png)
     ![image](https://user-images.githubusercontent.com/49571908/163294744-cef24d7f-91cc-472e-bb9b-431711afddc6.png)
     ![image](https://user-images.githubusercontent.com/49571908/163294785-ad2bdf42-24a5-4cec-a187-6a4b357de9a0.png)


    
