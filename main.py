import random
import time


# generovani jednotlivych neopakujicich random
# cisel do doby nez jsou po spojeni vetsi nez 999.
def generovani_cisla():
    cislo = 0
    jednotliva_cisla = [0, 0, 0, 0]
    while cislo < 999:
        jednotliva_cisla = random.sample(range(0, 9), 4)
        cislo_strings = [str(integer) for integer in jednotliva_cisla]
        spojeni_stringu = "".join(cislo_strings)
        cislo = int(spojeni_stringu)
    return jednotliva_cisla


def overeni_cisla_delka(delka_cisla):
    if len(delka_cisla) != 4:
        return True
    else:
        return False


def overeni_cisla_numeric(cislo_is_numeric):
    if cislo_is_numeric.isnumeric():
        return False
    else:
        return True


# cyklus projede jednotlive zadane cislo a kdyz jeste neni v promene, prida ho.
# pote se overi delka cisla, nebyla-li cisla unikatni, delka bude mensi.
def overeni_cisla_opakovani(cislo_opakovani):
    cislo = []
    for x in cislo_opakovani:
        if x not in cislo:
            cislo.append(x)
    if len(cislo) != 4:
        return True
    else:
        return False


def prepis_ze_string_do_listu(str_to_list):
    return [int(a) for a in str(str_to_list)]


# pomoci fce zip jsou sparovany cisla a nasledne se ptame zda je
# vybrane cislov  random cisle a kdyz ano, tak jestli jsou na stejne pozici
def bu_x_co_fce(cislo_rand, cislo_vybr):
    bu_x_co = [0, 0]
    for i, j in zip(cislo_rand, cislo_vybr):
        if j in cislo_rand:
            if j == i:
                bu_x_co[0] += 1
            else:
                bu_x_co[1] += 1
    return bu_x_co


print("""Hi there!
--------------------------------------------------
I've generated a random 4 digit number for you.
    Let's play a bulls and cows game. You have max. 20 tries.
-------------------------------------------------- """)

random_cislo = generovani_cisla()

pokus = 0
pocet_pokusu = 20
start = time.time()
while pokus < pocet_pokusu:
    vybrane_cislo = input("Enter a number: ")
    bulls_x_cows = [0, 0]
    pokus += 1

    if overeni_cisla_delka(vybrane_cislo):
        print("Number:", vybrane_cislo, "does not have four digits")
        continue

    if overeni_cisla_numeric(vybrane_cislo):
        print("Number:", vybrane_cislo, "contains non-numeric characters")
        continue

    if overeni_cisla_opakovani(vybrane_cislo):
        print("Numbers in", vybrane_cislo, "are not unique")
        continue

    vybrane_cislo = prepis_ze_string_do_listu(vybrane_cislo)

    if bu_x_co_fce(random_cislo, vybrane_cislo)[0] == 4:
        print("Correct, you've guessed the right number")
        print("in", pokus, "guesses!")
        end = time.time()
        print("Your time is:", round(end - start), "s")
        break

    print(bu_x_co_fce(random_cislo, vybrane_cislo)[0], "bulls", bu_x_co_fce(random_cislo, vybrane_cislo)[1], "cows")
    print("Remaining number of tries: ", pocet_pokusu - pokus)
else:
    print("Unfortunately, you've used up all your tries")
