def get_response( text ):
    text = text.lower()

    # Dictionary of responses
    q_a = {
        'amakuru': 'Amakuru ni meza, ayawe?',
        'mwaramutse': 'Mwaramutse neza! Amakuru?',
        'sawa': 'Sawa turasubira!',
        'umeze ute': 'Meze neza! Wowe se biragenda?',
        'ndarwaye': 'Yooo! Ihangane, ujye kwa muganga niba bikomeye.',
        'ndishimye': 'Nibyiza cyane, komeza wishime! Wambwira icyaguteye kwishima se?',
        'witwa nde': 'Nitwa Kinyarwanda Voice Assistant, ndi umufasha wubatswe kuri porogaramu, ngufasha mubyo ushaka kumenya.',
        'ukora iki': "Ntegura ibisubizo bitewe n'ibibazo umbajije.",
        'nkeneye ubufasha': 'Niteguye kugufasha, mbwira icyo ushaka ko ngufashamo.',
        'Rwanda Coding Academy iherereye he?': "Iherereye mu burengerazuba bw' u Rwanda, mu karere ka Nyabihu"
    }

    if text in q_a:
        return q_a[ text ]

    # Search for response
    for q in q_a:
        if q in text:
            return q_a[ q ]

    return 'Simbyumva neza, sobanura neza.'