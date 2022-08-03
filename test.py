

class Cats:
    test_voice = 'Miy'

    @classmethod
    def validate(cls, *args):
        return cls.test_voice

    def __init__(self, name: str, len_hair: int, tone_voice: str) -> None:
        self.name = name
        self.len_hair = len_hair
        self.tone_voice = tone_voice

    def __del__(self):
        print('Удаление: ' + str(self))

    def get_voice(tone_voice) -> str:
        return tone_voice

    def name_cat(self):
        return self.name


ct = Cats("Murka", 20, "Mey")
Cats.validate(2)
res = ct.name_cat()
print(res)
print(ct.__dict__)
