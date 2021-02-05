from django import forms 

class RegisterForm(forms.Form): 
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
    neighbourhoods = (
        ('Alamo Square','Alamo Square'),
        ('Anza Vista','Anza Vista'),
        ('Ashbury Heights','Ashbury Heights'),
        ('Balboa Park','Balboa Park'),
        ('Balboa Terrace','Balboa Terrace'),
        ('Bayview','Bayview'),
        ('Belden Place','Belden Place'),
        ('Bernal Heights','Bernal Heights'),
        ('Buena Vista','Buena Vista'),
        ('Butchertown (Old','Butchertown (Old'),
        ('Castro','Castro'),
        ('Cathedral Hill','Cathedral Hill'),
        ('Cayuga Terrace','Cayuga Terrace'),
        ('China Basin','China Basin'),
        ('Chinatown','Chinatown'),
        ('Civic Center','Civic Center'),
        ('Clarendon Heights','Clarendon Heights'),
        ('Cole Valley','Cole Valley'),
        ('Corona Heights','Corona Heights'),
        ('Cow Hollow','Cow Hollow'),
        ('Crocker-Amazon','Crocker-Amazon'),
        ('Design District','Design District'),
        ('Diamond Heights','Diamond Heights'),
        ('Dogpatch','Dogpatch'),
        ('Dolores Heights','Dolores Heights'),
        ('Duboce Triangle','Duboce Triangle'),
        ('Embarcadero','Embarcadero'),
        ('Eureka Valley','Eureka Valley'),
        ('Excelsior','Excelsior'),
        ('Fillmore','Fillmore'),
        ('Financial District','Financial District'),
        ('Fishermans Wharf','Fishermans Wharf'),
        ('Forest Hill','Forest Hill'),
        ('Forest Knolls','Forest Knolls'),
        ('Glen Park','Glen Park'),
        ('Golden Gate','Golden Gate'),
        ('Haight-Ashbury','Haight-Ashbury'),
        ('Hayes Valley','Hayes Valley'),
        ('Hunters Point','Hunters Point'),
        ('India Basin','India Basin'),
        ('Ingleside','Ingleside'),
        ('Ingleside Terraces','Ingleside Terraces'),
        ('Inner Sunset','Inner Sunset'),
        ('Irish Hill','Irish Hill'),
        ('Islais Creek','Islais Creek'),
        ('Jackson Square','Jackson Square'),
        ('Japantown','Japantown'),
        ('Jordan Park','Jordan Park'),
        ('Laguna Honda','Laguna Honda'),
        ('Lake Street','Lake Street'),
        ('Lakeside','Lakeside'),
        ('Lakeshore','Lakeshore'),
        ('Laurel Heights','Laurel Heights'),
        ('Lincoln Manor','Lincoln Manor'),
        ('Little Hollywood','Little Hollywood'),
        ('Little Russia','Little Russia'),
        ('Little Saigon','Little Saigon'),
        ('Lone Mountain','Lone Mountain'),
        ('Lower Haight','Lower Haight'),
        ('Lower Pacific','Lower Pacific'),
        ('Lower Nob','Lower Nob'),
        ('Marina District','Marina District'),
        ('Merced Heights','Merced Heights'),
        ('Merced Manor','Merced Manor'),
        ('Midtown Terrace','Midtown Terrace'),
        ('Mid-Market','Mid-Market'),
        ('Miraloma Park','Miraloma Park'),
        ('Mission Bay','Mission Bay'),
        ('Mission District','Mission District'),
        ('Mission Dolores','Mission Dolores'),
        ('Mission Terrace','Mission Terrace'),
        ('Monterey Heights','Monterey Heights'),
        ('Mount Davidson','Mount Davidson'),
        ('Nob Hill','Nob Hill'),
        ('Noe Valley','Noe Valley'),
        ('North Beach','North Beach'),
        ('North of','North of'),
        ('Oceanview','Oceanview'),
        ('Outer Mission','Outer Mission'),
        ('Outer Sunset','Outer Sunset'),
        ('Pacific Heights','Pacific Heights'),
        ('Parkmerced','Parkmerced'),
        ('Parkside','Parkside'),
        ('Parnassus','Parnassus'),
        ('Polk Gulch','Polk Gulch'),
        ('Portola','Portola'),
        ('Portola Place','Portola Place'),
        ('Potrero Hill','Potrero Hill'),
        ('Presidio','Presidio'),
        ('Presidio Heights','Presidio Heights'),
        ('Richmond District','Richmond District'),
        ('Rincon Hill','Rincon Hill'),
        ('Russian Hill','Russian Hill'),
        ('Saint Francis','Saint Francis'),
        ('Sea Cliff','Sea Cliff'),
        ('Sherwood Forest','Sherwood Forest'),
        ('Silver Terrace','Silver Terrace'),
        ('South Beach','South Beach'),
        ('South End','South End'),
        ('South of','South of'),
        ('South Park','South Park'),
        ('Sunnydale','Sunnydale'),
        ('Sunnyside','Sunnyside'),
        ('Sunset District','Sunset District'),
        ('Telegraph Hill','Telegraph Hill'),
        ('Tenderloin','Tenderloin'),
        ('Treasure Island','Treasure Island'),
        ('Twin Peaks','Twin Peaks'),
        ('Union Square','Union Square'),
        ('University Mound','University Mound'),
        ('Upper Market','Upper Market'),
        ('Visitacion Valley','Visitacion Valley'),
        ('Vista del','Vista del'),
        ('West Portal','West Portal'),
        ('Western Addition','Western Addition'),
        ('Westwood Highlands','Westwood Highlands'),
        ('Westwood Park','Westwood Park'),
        ('Yerba Buena','Yerba Buena'),
    )
    neighbourhoods= forms.ChoiceField(
        label='What is your neighborhood?', 
        choices=neighbourhoods
        )
    city_name = forms.CharField(widget=forms.Textarea)
    state_name = forms.CharField(widget=forms.Textarea)
    interested_in_friends = forms.BooleanField(required=False)

