def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Əgər element integer deyilsə, ValueError çıxacaq → except skip edir
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # integer olmayanları səssiz skip edirik
            pass
        except IndexError:
            # tapşırığa görə IndexError buraxılmalıdır
            raise
    print()  # yeni sətir
    return count
