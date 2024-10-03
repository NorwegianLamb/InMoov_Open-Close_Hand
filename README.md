# InMoov_Open-Close_Hand
<p align="center">
  <img src="https://github.com/user-attachments/assets/016c200e-f48a-4107-b3a2-5134c767d68c" />
</p>

These are the **5 servo motors** that control the fingers of the **InMoov Hand**, there is also an hidden one in the wrist but it will not be included in this project.

To start, we need to connect the **yellow pin** of the servos to the various GPIO output pins of the Raspberry PI, remember which GPIO pins you chose because we'll need to manage every one of them in the code.

I reccomend using an external battery to power all the motors, using the 5V supply of the raspberry can cause problems based on the amount of servos attached or the type of motors.

## Setup the GPIO pins:
Now that we wired everything we need to specify the GPIO pins we used with the following snippet:
```
GPIO.setup(pin[i], GPIO.OUT)
```
The rest of the code specifies the **frequency** and the **duty cycle** of the fingers to manage the **servo's position/rotation**.

## Results:
This is an example of running the code, **I volunteerly selected 1 duty-cycle per second** to show you all of its movements (you can, of course, **select a faster cycle** to have a smooth movement).
<div align="center">
  <video src="https://github.com/user-attachments/assets/9d59aa13-8255-4aba-8b2d-7a78535746e5" />
</div>
    
You could spice it up by adding **ECG electrodes** to your forearm and catch the electrical signal fired by your neurons when opening/closing your hand and use that to **control the robotic arm** :)
