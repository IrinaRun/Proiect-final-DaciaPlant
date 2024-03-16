Descrierea proiectului

	Pentru proiect am ales sa testez site-ul www.daciaplant.ro (un site de vanzare produse naturiste) folosind testare automata cu ajutorul librariei unittest

Framework folosit

	Am folosit testarea automata cu ajutorul librariei unittest.
Testarea automata este importanta deoarece permite realizarea unui numar mare de teste intr-un timp mai scurt decat la testarea manuala. Ea ajuta la marirea productivitatii.

Tools

	In cadrul proiectului am folosit limbajul de programare Python si am utilizat IDE-ul PyCharm pentru a dezvolta si rula codul. Python este un un limbaj de programare popular, cunoscut pentru simplitatea sa. PyCharm este un mediu de dezvoltare integrat (IDE) specializat pentru dezvoltarea in Python, oferind un set bogat de functionaloitati si instrumente.
	Pentru a dezvolta si rula codul am folosit urmatoarele librarii:
- unittest – am importat modulul unitttest care furnizeaza un framework pentru testarea automata si manuala
- Time – am importat acest modul pentru a utiliza functia Sleep. Modulul nu necesita instalare suplimentara
- Selenium: Am utilizat modulul selenium.common pt a importa clasa NoSuchElementException si modulul seleniu.webdriver.common.by pt a importa clasa By
- Selenium.webdriver.support: am importat modulul WebDriverWait si modulul expected_conditions - pentru a astepta conditii specifice in timpul rularii testelor. Sunt instalate in libraria Selenium si nu necesita instalare separata.
- Browser – am utilizat acest modul pentru a controla interactiunea cu browserul web
Pentru instalarea librariilor se foloseste comanda pip install <nume-librarie> in linia de comanda (de ex selenium)

Teste

	Testele realizate pe aplicatia aleasa au fost urmatoarele:
- am testat ca se poate face logarea in cont cu date corecte
- am testat ca se afiseaza un mesaj de eroare daca se incearca logarea cu credentiale gresite
- am testat ca se poate face cautarea unui anumit produs (‘vitamina C’) 
- am testat  ca nr de produse gasite este mai mare de 10
- am testat ca se poate naviga si alege o anumita categorie (‘Antistres) si in cadrul categoriei alese se poate selecta o subcategorie (‘Insomnie’) 
- am testat ca in aceasta subcategorie sunt afisate minim 3 produse
- am testat ca se poate adauga un produs in cos
- am testat ca se poate sterge un produs din cos
- am testat ca se poate face delogarea din cont
- am testat ca se poate adauga un produs la favorite

  Instalarea proiectului
  
  Pentru a utiliza proiectul, urmați acesti pași:
  
 	Clonarea proiectului : Executați comanda git clone https://github.com/IrinaRun/Proiect-final-DaciaPlant.git . Aceasta va crea o copie locală a proiectului pe computerul dvs.
  
 	Instalarea dependențelor: Executați comanda pip install -r requirements.txt pentru a instala toate librăriile și dependențele necesare proiectului.
  
	Rularea testelor: rulați comanda python –m unittest pentru a executa scenariile de test






