import pickle
sim_chars = pickle.load(open('/home/james/patent/data/char_sims.pkl', 'rb'))

sims = {}
for pair in sim_chars:
    if sim_chars[pair][1] > 0.91:
        if pair[0] not in sims:
            sims[pair[0]] = [pair[1]]
        else:
            sims[pair[0]] += [pair[1]]
