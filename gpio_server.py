import pigpio
import time
import math

pi = pigpio.pi()

class ServoController:
	def __init__(self, gpio):
                pi.set_mode(18, pigpio.OUTPUT)
		self.gpioPin = gpio
		self.angle = 0
                self.dutyCycle = 6
                pi.set_PWM_range(18, 100)
                pi.set_PWM_frequency(18, 100)

	def setAngle(self, degrees):
		
		if degrees > 180:
			degrees = 180
		elif degrees < 0:
			degrees = 0

                duty = (degrees / 10.0 + 6.5)

                pi.set_PWM_dutycycle(18, duty)
		time.sleep(0.1)
		self.angle = degrees
                self.dutyCycle = duty
        
        def setDutyCycle(self, dutyCycle):
                if dutyCycle > 25:
                        dutyCycle = 25
                elif dutyCycle < 6:
                        dutyCycle = 6
                pi.set_PWM_dutycycle(18, dutyCycle)
                time.sleep(0.1)
                self.dutyCycle = dutyCycle
		
	def incAngle(self, increment):
		self.setAngle(self.angle + increment)
                time.sleep(0.1)
                self.angle = self.angle + increment

        def incDutyCycle(self, increment):
                self.setDutyCycle(self.dutyCycle + increment)
	        time.sleep(0.1)
                self.dutyCycle = self.dutyCycle + increment

        def cleanup(self):
                pi.stop()
