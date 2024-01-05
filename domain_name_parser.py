def domain_url(url):
    colon = 0
    domain = ''
    for i in range(len(url)):
        if url[i] == ':':
            colon = i + 3
            break

    if url[colon] == 'w' and url[colon + 1] == 'w' and url[colon + 2] == 'w':
        colon += 4

    for i in range(colon, len(url)):
        if url[i] == '.':
            break
        domain += url[i]

    return domain

print(domain_url("https://www.google.com"))
print(domain_url("https://github.com"))
print(domain_url("http://www.zombie-bites.com"))
print(domain_url("https://www.cnet.com"))
