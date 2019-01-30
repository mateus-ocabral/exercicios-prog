times=('Real Madrid','Barcelona','Bayern','Juventus','Milan','Boca','Manchester','Benfica','Porto','Santos', 'Sao Paulo')

print('Os melhores times sao: {}'.format(times))
print("Os tres melhores sao {}".format(times[0:3]))
print("Os tres ultimos sao {}".format(times[len(times)-3:len(times)]))

print('Os times em ordem alfabetica sao: {}'.format(sorted(times)))