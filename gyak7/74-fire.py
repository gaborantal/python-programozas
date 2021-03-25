import datetime
import fire


def pentek13(elmult_evek):
    """
    Az utóbbi hány évben számoljuk ki a péntek 13-ak számát.
    :param elmult_evek: az elmúlt évek száma
    :return: hányszor volt péntek 13
    """
    most = datetime.date.today()
    mikortol = most.year - elmult_evek

    ev_szamlalo = dict()

    for ev in range(mikortol, most.year):
        for honap in range(1, 13):
            datum_13 = datetime.date(ev, honap, 13)
            if datum_13.weekday() == 4:
                if datum_13.year not in ev_szamlalo:
                    ev_szamlalo[datum_13.year] = 0
                ev_szamlalo[datum_13.year] += 1

    return ev_szamlalo


if __name__ == '__main__':
    fire.Fire(pentek13)
