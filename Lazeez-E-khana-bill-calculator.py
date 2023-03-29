print(" Welcome to Lazeez-E-Khana  \n\n **Below is the Lazeez-E-Khana menu we have for you** \n\n" ,
      "--Lazeez Food Items--                     --Cost--  \n\n",
      "1. Veg Sandwich                            $2.99 \n",
      "2. Non-Veg Sandwich                        $3.99 \n",
      "3. Chicken Shawarma                        $8.99 \n",
      "4. Beef Shawarma                           $9.99 \n",
      "5. Mixed Shawarma                          $11.99 \n",
      "6. Green Salad                             $2.99 \n",
      "7. Caesar Salad                            $3.99 \n",
      "8. Lazeez Special                          $19.99 \n" )
tax=0.08

cost = {'Veg_Sandwich': 2,'Non_Veg_Sandwich': 3,
        'Chicken_Shawarma': 8,'Beef_Shawarma': 9,
        'Mixed_Shawarma': 11,'Green_Salad': 2,
        'Caesar_Salad': 3,'Lazeez_Special': 19}
print("Enter the items you want to order.")
Veg_Sandwich=int(input("Veg Sandwich:"))
Non_Veg_Sandwich=int(input("Non Veg Sandwich:"))
Chicken_Shawarma=int(input("Chicken Shawarma:"))
Beef_Shawarma=int(input("Beef Shawarma:"))
Mixed_Shawarma=int(input("Mixed Shawarma:"))
Caesar_Salad=int(input("Caesar Salad:"))

fin_cost=Veg_Sandwich*cost["Veg_Sandwich"]+Non_Veg_Sandwich*cost["Non_Veg_Sandwich"]+Chicken_Shawarma*cost["Chicken_Shawarma"]+Beef_Shawarma*cost["Beef_Shawarma"]+Mixed_Shawarma*cost["Mixed_Shawarma"]+Caesar_Salad*cost["Caesar_Salad"]
Bill=cost+tax
print("Please pay $ %f" %Bill)
total = sum(cost.values())
