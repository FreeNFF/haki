from audioop import avg
import requests
import json

api_url = "https://restcountries.com/v3.1/all"#adrese

try:#get pieprasījums uz API
    response = requests.get(api_url)

    if response.status_code == 200:#pārbauda vai pieprasījums ir veiksmīgs (status kods 200)
        countries_data = response.json()

        #izvada visu valsts nosaukumus
        print("Visu valstu nosaukumi: ")
        for country in countries_data:
            country_name = country.get("name", {}).get("common", "Nezināms nosaukums")
            print(country_name)
        
        #izveido kopējo valsts nosaukumu
        valsts_daudzums = len(country_name)
        print(f"Kopā ir {valsts_daudzums} valstis.")

        total_population = sum(country.get("population", 0) for country in countries_data)
        #avarega_civilians = avg(total_popilation)
        average_population = total_population / valsts_daudzums if valsts_daudzums else 0
        print(f"\nVidējais iedzīvotāju skaits visās valstīs: {average_population:,.0f}")

        #izvada valsti ar visvairāk iedzīvotājiem
        largest_pop_c = max(countries_data, key=lambda x: x.get("population", 0))
        largest_pop_n = largest_pop_c.get("name", {}).get("common","Nezināms nosaukums")
        largest_pop = largest_pop_c("population", 0)
        print(f"Valsts ar visvairāk iedzīvotājiem un to skaitu: {largest_pop_n} ({largest_pop:,.0}) iedzīvotāji")

        #izvada visu valstu kopējo platību
        total_area = sum(country.get("area", 0) for country in countries_data)
        print(f"\n Visu valstu kopējā platība: {total_area:,.0} kvadrātkilometri")

        latvia_info = next((country for country in countries_data if country.get("name", {}).get ("common")=="Latvia"), None) 