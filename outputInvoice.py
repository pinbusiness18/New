Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: /Users/chumpawhumps/Desktop/Summer 2021-Python/InvoiceProgram#2.py =
Hello!

Please enter Customer ID:AF101

Number of box of Milk Chocolate @ $8.50: 1

Number of box of Dark European @ $9.75: 0

Number of box of White Chocolate @ $10.50: 1

Number of box of European Truffles @ $12.50: 3

-----------------------------------------------

Invoice for Customer AF101:

1 Milk Chocolate @ $8.50 is $8.50
0 Dark European @ $9.75 is $0.00
1 White Chocolate @ $10.50 is $10.50
3 European Truffles @ $12.50 is $37.50

Subtotal              $56.50
Sales Tax @ 9.5%      $5.37
Shipping @ 10.0%      $5.65

Grand Total           $67.52

-----------------------------------------------
>>> 
== RESTART: /Users/chumpawhumps/Desktop/Summer 2021-Python/InvoiceProgram#2.py =
Hello!

Please enter Customer ID:Sonia Pineda33

Number of box of Milk Chocolate @ $8.50: 1.5
Traceback (most recent call last):
  File "/Users/chumpawhumps/Desktop/Summer 2021-Python/InvoiceProgram#2.py", line 14, in <module>
    milkChoco = int(input("\nNumber of box of Milk Chocolate @ $8.50: "))
ValueError: invalid literal for int() with base 10: '1.5'
>>> 
== RESTART: /Users/chumpawhumps/Desktop/Summer 2021-Python/InvoiceProgram#2.py =
Hello!

Please enter Customer ID:SoSo33!

Number of box of Milk Chocolate @ $8.50: 1

Number of box of Dark European @ $9.75: 0

Number of box of White Chocolate @ $10.50: 12

Number of box of European Truffles @ $12.50: 10

-----------------------------------------------

Invoice for Customer SoSo33!:

1 Milk Chocolate @ $8.50 is $8.50
0 Dark European @ $9.75 is $0.00
12 White Chocolate @ $10.50 is $126.00
10 European Truffles @ $12.50 is $125.00

Subtotal              $259.50
Sales Tax @ 9.5%      $24.65
Shipping @ 10.0%      $25.95

Grand Total           $310.10

-----------------------------------------------
>>> 