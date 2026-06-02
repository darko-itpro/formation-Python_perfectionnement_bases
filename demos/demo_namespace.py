
network = get_network()

if network:
    import webservice as service
else:
    import cache as service

service.save(data)
service.save(data)