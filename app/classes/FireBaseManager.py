from sys import stderr
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from app.classes import User
import pyrebase
class FireBaseManager():
    firestoreManager=""
    pyrebaseManager=""
    def __init__(self):
        cred = credentials.Certificate('credentials.json')
        firebase_admin.initialize_app(cred,{
            'storageBucket': "seguridadproyecto-2a366.appspot.com"
        })
        self.firestoreManager=firestore.client()
        config = {
        "apiKey": "AIzaSyAryxJPGDbzH8PmZKITRgB9y5wQWw69cNw",
        "authDomain": "seguridadproyecto-2a366.firebaseapp.com",
        "databaseURL": "https://seguridadproyecto-2a366-default-rtdb.firebaseio.com/",
        "storageBucket": "seguridadproyecto-2a366.appspot.com",
        "serviceAccount": "credentials.json"
        }

        self.pyrebaseManager = pyrebase.initialize_app(config)
    def refreshToken(self,refreshT):
        auth = self.pyrebaseManager.auth()
        return auth.refresh(refreshT)
    def loginUsuario(self, mail, password):
        auth = self.pyrebaseManager.auth()
        try:
            user=auth.sign_in_with_email_and_password(mail, password)
            nombre=self.getUsuarioByID(user["localId"])["nombreCompleto"]
            myUser=User.User(user["email"],nombre,user["localId"],user["idToken"],user["refreshToken"],int(user["expiresIn"]),self)
            print("USER:\n\n", myUser.correo, file=stderr)
            return myUser
        except Exception as e:
            print("ERROR LOGIN\n\n:", str(e), file=stderr)
            return False
    def registraUsuario(self, nombre, mail, password, fecha, especializacion, institucion, pais, estado):
        auth = self.pyrebaseManager.auth()
        try:
            user=auth.create_user_with_email_and_password(mail, password)
            id=user["localId"]
            newValues={
                "nombreCompleto":nombre,
                "email":mail,
                "UID":id,
                "fechaNacimiento":fecha,
            }
            self.firestoreManager.collection(u'usuarios').document(id).set(newValues)
            myUser=User.User(mail,nombre,id,"a","a",1000,self)
            print("USER:\n\n", myUser.correo, file=stderr)
            return myUser
        except Exception as e:
            print("ERROR REGISTRO\n\n:", str(e), file=stderr)
            return False
    
    def getUsuarioByID(self, idUsuario):
        usuariosRef=self.firestoreManager.collection(u'usuarios')
        query = usuariosRef.where(u'UID', u'==', idUsuario).get()
        if len(query)==0: return False
        usuario=query[0].to_dict()
        return usuario
    def getUsuarios(self):
        usuarios=[]
        usuariosQuery=self.firestoreManager.collection("usuarios").get()
        for usuario in usuariosQuery:
            usuarioDict=usuario.to_dict()
            usuarios.append(usuarioDict)
        return usuarios

    def getOtherUser(self):
        users=[]
        usersQuery=self.firestoreManager.collection("usuarios").get()
        for user in usersQuery:
            userDict=user.to_dict()
            users.append(userDict)
        return users

    def getFollowingByID(self,idFollowing,idUsuario):
        following=self.getFollowingFromUsuario(idUsuario)
        print("FOLLOWING:\n\n",following,file=stderr)
        for user in following:
            if int(user["idNum"])==int(idFollowing):
                print("FOLLOWING ENCONTRADO:\n\n",user,file=stderr)
                return user
        return False

    def getFollowingFromUsuario(self, idUsuario):
        following=[]
        followingRef=self.firestoreManager.collection(u'usuarios').document(idUsuario).collection("following").get()
        for uFollowing in followingRef:
            print("QUERIES:\n\n",uFollowing.to_dict(),file=stderr)
            followingDict=uFollowing.to_dict()
            following.append(followingDict)
        if len(following)==0: return False
        return following
    
    def getFollowerByID(self,idFollower,idUsuario):
        follower=self.getFollowerFromUsuario(idUsuario)
        print("FOLLOWING:\n\n",follower,file=stderr)
        for user in follower:
            if int(user["idNum"])==int(idFollower):
                print("FOLLOWER ENCONTRADO:\n\n",user,file=stderr)
                return user
        return False

    def getFollowerFromUsuario(self, idUsuario):
        followers=[]
        followerRef=self.firestoreManager.collection(u'usuarios').document(idUsuario).collection("followers").get()
        for follower in followerRef:
            print("QUERIES:\n\n",followerRef.to_dict(),file=stderr)
            followerDict=follower.to_dict()
            followers.append(followerDict)
        if len(followers)==0: return False
        return followers
    
    def modificarTweet(self, id, idTweet, nuevoTweet):
        tweetsRef=self.firestoreManager.collection(u'usuarios').document(id).collection("tweets")
        query = tweetsRef.where(u'idNum', u'==', int(idTweet)).get()
        field_updates = {"contenido":nuevoTweet, "fecha":""}
        for tweet in query:
              
            doc = tweetsRef.document(tweet.id)
            doc.update(field_updates)
            return True
        return False
 
