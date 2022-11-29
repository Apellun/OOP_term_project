from dataclasses import dataclass

@dataclass
class Skill():
    name: str = NotImplemented
    attack: int = NotImplemented
    stamina: int = NotImplemented

    # @abstractmethod
    # def skill_effect(self):
    #     """
    #     метод должен быть переопределён при создании
    #     сабклассов с конкретными умениями
    #     """
    #     pass

    # def use(self, user, target):
    #     if user.stamina >= self.stamina:
    #         return self.skill_effect()
    #     return "выносливости недостаточно"

    

ferocious_kick = Skill(name = "Свирепый пинок", attack = 12, stamina = 6)
powerful_sting = Skill(name = "Мощный укол", attack = 15, stamina = 5)