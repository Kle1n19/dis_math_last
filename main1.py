import random

class Simulate:
    def __init__(self):
        self.sleep = self.sleep()
        self.eat = self.eat()
        self.study = self.study()
        self.dota = self.dota()
        self.gym = self.gym()

        self.relax = self.relax()
        self.deadline = self.deadline()
        self.come_for_sja = self.come_for_sja()

        self.current_state = self.sleep

        next(self.sleep)
        next(self.eat)
        next(self.study)
        next(self.dota)
        next(self.gym)
        next(self.relax)
        next(self.deadline)
        next(self.come_for_sja)

    def sleep(self):
        while True:
            time = yield
            print(f'Hour {time}')
            print('State: Sleep')
            print('-'*30)
            if time in range(8):
                    self.current_state = self.sleep
            self.current_state = random.choice([self.eat, self.study])

    def eat(self):
        while True:
            time = yield
            print(f'Hour {time}')
            print('State: Eat')
            print('-'*30)
            if random.random() > 0.5:
                self.current_state = self.eat
            else:
                self.current_state = random.choice([self.sleep, self.come_for_sja])

    def study(self):
        while True:
            time = yield
            print(f'Hour {time}')
            print('State: Study')
            print('-'*30)
            if random.random() > 0.3:
                self.current_state = self.study
            else:
                self.current_state = random.choice([self.eat, self.gym])

    def dota(self):
        while True:
            time = yield
            print(f'Hour {time}')
            print('State: Play Dota')
            print('-'*30)
            if time in range(14, 15):
                if random.random() > 0.4:
                    self.current_state = self.dota
                else:
                    self.current_state = self.study
            else:
                self.current_state = random.choice([self.eat, self.sleep])

    def gym(self):
        while True:
            time = yield
            print(f'Hour {time}')
            print('State: PUMP')
            print('-'*30)
            if random.random() > 0.7:
                self.current_state = self.gym
            else:
                self.current_state = self.study


    def relax(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print("State: Studying is hard))))0)))0)0000))))0)")
            print('-'*30)
            if time in range(22,24):
                self.current_state = self.relax
            else:
                self.current_state = self.sleep

    def deadline(self):
        while True:
            time = yield
            print(f'Hour {time}')
            print("State: oh,NOOOOOOOOOOOOOo")
            print('-'*30)
            if random.random() > 0.9:
                self.current_state = self.relax
            else:
                self.current_state = self.deadline

    def come_for_sja(self):
        while True:
            time = yield
            print(f'\nHour {time}')
            print("State: Come for SJa (Impossible)")
            print('-'*30)
            if random.random() != 1:
                self.current_state = self.dota
            else:
                self.current_state = self.come_for_sja
    
    def cycle(self):
        for i in range(1,25):
            self.current_state.send(i)


fsm = Simulate()
fsm.cycle()