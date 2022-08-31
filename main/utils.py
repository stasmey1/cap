from .models import *
import random

old_country = [None]
old_capital = [None]
group_global = None


class Game:
    def __init__(self):
        if str(group_global).isdigit():
            self.country_set = Country.objects.filter(group_id=group_global)
        else:
            self.country_set = Country.objects.all()
        self.country = random.choices(self.country_set)[0]
        old_country.append(self.country)
        old_capital.append(self.country.capital)

    def cap_list_limited(self):
        capitals = [i.capital for i in self.country_set if i.capital != self.country.capital]
        random.shuffle(capitals)
        cap_list_limited = capitals[:3]
        cap_list_limited.append(self.country.capital)
        random.shuffle(cap_list_limited)
        return cap_list_limited



