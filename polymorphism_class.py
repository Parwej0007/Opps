class INDIA :

    def Capital(self) :
        print("capital of india is DELHI")
    def Language(self) :
        print("Language is HINDI")

class USA :
    def Capital(self) :
        print("capital of USA is WASINGTON DC")
    def Language(self) :
        print("Language ENGLISH")
    
obb1 = INDIA()
obb2 = USA()

for country in (obb1,obb2) :
    country.Capital()
    country.Language()