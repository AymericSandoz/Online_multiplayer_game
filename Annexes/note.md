# Note

## COmphéhension

C'est quoi une socket ?
Une socket est une abstraction logicielle qui représente une extrémité d'une connexion de réseau bidirectionnelle. Elle permet à des ordinateurs de communiquer les uns avec les autres sur un réseau, que ce soit sur une même machine (communication locale) ou à travers un réseau étendu (communication sur Internet). Les sockets sont largement utilisées pour établir des connexions réseau, envoyer et recevoir des données, et permettre la communication entre des machines distantes.

Concrètement, une socket est une interface qui permet aux programmes informatiques d'envoyer et de recevoir des données sur un réseau. Voici quelques caractéristiques importantes des sockets :

1. **Adressage** : Chaque socket est identifiée par une adresse IP et un numéro de port. L'adresse IP indique l'emplacement de l'ordinateur sur le réseau, et le numéro de port indique l'application ou le service spécifique sur cet ordinateur qui souhaite communiquer.

2. **Communication bidirectionnelle** : Une socket permet la communication bidirectionnelle, ce qui signifie qu'elle peut être utilisée pour envoyer des données et en recevoir en retour. Cela permet l'échange d'informations entre les parties qui utilisent la socket.

3. **Protocoles réseau** : Les sockets sont mises en œuvre en utilisant différents protocoles réseau, tels que TCP (Transmission Control Protocol) pour une communication fiable et orientée connexion, ou UDP (User Datagram Protocol) pour une communication non fiable et sans connexion.

4. **Types de sockets** : Il existe différents types de sockets, notamment les sockets de serveur et les sockets de client. Les sockets de serveur écoutent les connexions entrantes et acceptent les clients, tandis que les sockets de client établissent des connexions avec des serveurs.

5. **API de programmation** : Les sockets sont généralement utilisées à travers une API (Interface de Programmation d'Application) fournie par le système d'exploitation ou des bibliothèques logicielles, telles que l'API socket en Python. Cette API offre des fonctions pour créer, configurer, et utiliser les sockets.

En résumé, une socket est un outil essentiel pour établir des connexions réseau, que ce soit pour la communication sur Internet, la création de serveurs, la communication entre applications sur la même machine, ou d'autres scénarios de réseau. Elle permet de transférer des données de manière fiable et efficace entre des ordinateurs et des applications.


`AF_INET` et `SOCK_STREAM` sont des constantes utilisées dans le contexte de la programmation réseau pour spécifier le domaine de communication et le type de socket à utiliser lors de la création d'une socket avec la bibliothèque de sockets, comme celle de Python.

1. `AF_INET` : Cela signifie "Address Family - Internet". C'est une constante qui indique que vous créez une socket qui fonctionne avec le protocole IPv4, qui est le protocole de communication Internet le plus couramment utilisé. En d'autres termes, `AF_INET` spécifie que la socket sera utilisée pour la communication sur Internet avec des adresses IP version 4.

2. `SOCK_STREAM` : Cela signifie "Socket Type - Stream". C'est une constante qui indique que vous créez une socket de type flux. Les sockets de type flux utilisent le protocole TCP (Transmission Control Protocol), qui est un protocole de communication orienté connexion. Les sockets de type flux fournissent une communication fiable, où les données sont envoyées dans l'ordre et sans perte, ce qui est essentiel pour de nombreuses applications, comme les transferts de fichiers, les connexions sécurisées, etc.

En résumé, `AF_INET` spécifie le protocole Internet IPv4, et `SOCK_STREAM` spécifie le type de socket de flux, utilisant le protocole TCP. Ces constantes permettent de configurer correctement la socket pour la tâche spécifique que vous souhaitez accomplir en fonction du type de communication et du protocole réseau requis.



192.168.1.75

La vitesse du velo doit etre egale à 2 sinon ça crée des bugs d'alignement(hitbox). 4 ça passe mais 3 c'est horrible.  
Les autres sprite, avant d'être controlés par quelqu'un, ne sont pas paraitement alignés car il ne subissent pas encore self.player.align_hitbox

  reply = players # players[:player] + players[player+1:]
Le fait de mettre players a régler le soucis de l'affichage du bonhomme en haut à gauche mais à créer un nouveau soucis d'affichage de doublon dans la maison lol wtf

  # intéressant si je laisse juste players instances il y a u bonhomme en haut à gauche
        self.map.add_characters(player_instances[0:(len(player_instances)-1)])


# en y de 368 à 338 il y a un bug les autres perso ne décale
# e x de 636 à 668