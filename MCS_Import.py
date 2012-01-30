def MCS_import(file_name):

    f = open(file_name, 'rb')
    f.readline()
    f.readline()
    sampling_rate = float(f.readline()[14:-2])
    ADC_zero = float(f.readline()[11:-2])
    El = float(f.readline()[5:11])
    channel_names = f.readline()[10:].split(';')
    channel_names[-1] = channel_names[-1][:-2]
    f.readline()

    from numpy import fromfile

    data = fromfile(f, dtype='uint16')
    data = data.reshape((len(channel_names),-1), order='F')

    for i in range(len(channel_names)):
        if channel_names[i].startswith('El'):
            data[i] = (data[i]-ADC_zero)*El

    return data, sampling_rate, channel_names
