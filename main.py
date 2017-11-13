

import folium
def inisiasi(long,lat):
	map_1 = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Terrain')
	return map_1
	
def hitam(long,lat):
	c = folium.Map(
    location=[long,lat],
    zoom_start=12,
    tiles='Stamen Toner')	
	return c

def masukkin(apa,ini):
	d = folium.Map(
	location=[apa,ini],
	zoom_start=12,
    tiles='Stamen Terrain')	
	return d
	
def simpan(anu,gede):
	anu.save(gede)

d = masukkin(-2.9521793,104.7499501)
c = hitam(-2.9521793,104.7499501)
map_1 = inisiasi(-2.9521793,104.7499501)
tooltip = 'Click me!'


folium.Marker([-2.952245, 104.758104], popup='pecel lele').add_to(map_1)
folium.Marker([-2.958722, 104.766448], popup='palembang golf club').add_to(map_1)
folium.Marker([-2.958754, 104.770375], popup='kopitiam').add_to(map_1)
folium.Marker([-2.958497, 104.770375], popup='the kitchen').add_to(map_1)
folium.Marker([-2.958379, 104.767178], popup='resto golf view').add_to(map_1)
folium.Marker([-2.962129, 104.769860], popup='baby store').add_to(map_1)
folium.Marker([-2.960500, 104.771502], popup='wisma grand kemala').add_to(map_1)
folium.Marker([-2.962225, 104.772950], popup='SMP negeri 4 palembang').add_to(map_1)
folium.Marker([-2.962311, 104.773465], popup='SMP negeri 50').add_to(map_1)
folium.Marker([-2.963350, 104.773240], popup='dexa medika').add_to(map_1)
folium.Marker([-2.994395, 104.725882], popup='Bukit Lama').add_to(map_1)
folium.Marker([-3.036781, 104.761596], popup='Kemas Rindo').add_to(map_1)
folium.Marker([-2.886206, 104.695321], popup='Talang Betutu').add_to(map_1)
folium.Marker([-2.906891, 104.716860], popup='Kebun Bunga').add_to(map_1)
folium.Marker([-2.919302, 104.781478], popup='Sako Baru').add_to(map_1)
folium.Marker([-2.984661, 104.842783], popup='Sei Lais').add_to(map_1)
folium.Marker([-2.951568, 104.686208], popup='Talang Klp.').add_to(map_1)
folium.Marker([-2.945777, 104.676266], popup='Bukit Baru').add_to(map_1)
folium.Marker([-3.033246, 104.738905], popup='Kemang Agung').add_to(map_1)
folium.Marker([-3.034244, 104.808871], popup='Plaju Darat').add_to(map_1)
folium.Marker([-2.991770, 104.763509], popup= 'Jembatan Ampera').add_to(map_1)
folium.Marker([-2.952395, 104.760451], popup= 'BPJS Kesehatan KC Palembang').add_to(map_1)
folium.Marker([-2.952572, 104.758477], popup= 'Warung Tenda Taichan').add_to(map_1)
folium.Marker([-2.952454, 104.757989], popup= 'BNI Kanten').add_to(map_1)
folium.Marker([-2.952068, 104.756621], popup= 'Pasar Buah Larisa').add_to(map_1)
folium.Marker([-2.951372, 104.761159], popup= 'Jco Donuts & Coffee').add_to(map_1)
folium.Marker([-2.954447, 104.762876], popup= 'SMK Telenika').add_to(map_1)
folium.Marker([-2.952958, 104.755146], popup= 'Istana Baterry').add_to(map_1)
folium.Marker([-2.952315, 104.754668], popup= 'Waroeng Steak Angkatan 66 Palembang').add_to(map_1)
folium.Marker([-2.949004, 104.753359], popup= 'Rumah Makan Rang Tanjung').add_to(map_1)
folium.Marker([-2.945506, 104.752946], popup= 'Warung Prasmanan Fifi').add_to(map_1)
folium.Marker([-2.995767, 104.742287], popup= 'PDAM Tirta Musi').add_to(map_1)
folium.Marker([-2.997459, 104.725537], popup= 'Bukit Siguntang').add_to(map_1)
folium.Marker([-2.989041, 104.719303], popup= 'Pondok Bontet').add_to(map_1)
folium.Marker([-2.981729, 104.715854], popup= 'Agen Rental Mobil Ampera').add_to(map_1)
folium.Marker([-2.983268, 104.733248], popup= 'Politeknik Negeri Sriwijaya').add_to(map_1)
folium.Marker([-2.987591, 104.728680], popup= 'Edelweis Ogan Palembang').add_to(map_1)
folium.Marker([-2.990874, 104.728811], popup= 'Wisma Sriwijaya').add_to(map_1)
folium.Marker([-2.992144, 104.727322], popup= 'Rumah Makan Siji').add_to(map_1)
folium.Marker([-2.991941, 104.727662], popup= 'Toko Buku Bina Ilmi').add_to(map_1)
folium.Marker([-2.993145, 104.728840], popup= 'Avana Florist').add_to(map_1)
folium.Marker([-2.993526, 104.824475], popup= 'General Hospital').add_to(map_1)
folium.Marker([-2.996176, 104.823048], popup= 'SMA Patra Mandiri').add_to(map_1)
folium.Marker([-2.991671, 104.825114], popup= 'Musholla Al-Ikhlas').add_to(map_1)
folium.Marker([-2.991575, 104.823354], popup= 'Gedung Patra Ogan').add_to(map_1)
folium.Marker([-2.991778, 104.822453], popup= 'Pertamina').add_to(map_1)
folium.Marker([-2.994253, 104.823698], popup= 'Wisma Pertamina Plaju').add_to(map_1)
folium.Marker([-2.992003, 104.821841], popup= 'Bowling Alley').add_to(map_1)
folium.Marker([-2.996996, 104.825350], popup= 'Balai Ria').add_to(map_1)
folium.Marker([-2.997875, 104.826026], popup= 'Gedung Aneka').add_to(map_1)
folium.Marker([-2.999203, 104.826133], popup= 'Musicool Futsal').add_to(map_1)
folium.Marker([-2.998785, 104.824599], popup= 'Masjid Jauharul Iman').add_to(map_1)
folium.Marker([-2.929380, 104.769420], popup= 'Unnamed Road').add_to(map_1)
folium.Marker([-2.932016, 104.759227], popup= 'SLB B YPAC Palembang').add_to(map_1)
folium.Marker([-2.935903, 104.783738], popup= 'Nasi Goreng Merah Newbee').add_to(map_1)
folium.Marker([-2.939929, 104.783452], popup= 'Daphu Kupi Dan Mie Aceh').add_to(map_1)
folium.Marker([-2.938069, 104.780020], popup= 'TJM FAC').add_to(map_1)
folium.Marker([-2.936915, 104.782938], popup= 'Swakarya Insan Mandiri. PT').add_to(map_1)
folium.Marker([-2.934609, 104.780854], popup= 'Raja Keripik').add_to(map_1)
folium.Marker([-2.934091, 104.783213], popup= 'Masjid Al Kautsar').add_to(map_1)
folium.Marker([-2.933005, 104.781851], popup= 'Sanggar Tari Mutiara').add_to(map_1)
folium.Marker([-2.932480, 104.784833], popup= 'Masjid Al-Ikhlas').add_to(map_1)
folium.Marker([-2.886332, 104.716994], popup='Talang Jambe').add_to(map_1)
folium.Marker([-2.913077, 104.683348], popup='Sukodadi').add_to(map_1)
folium.Marker([-2.915135, 104.692275], popup='Alang Alang Lebar').add_to(map_1)
folium.Marker([-2.872915, 104.696095], popup='SD Negeri 142').add_to(map_1)
folium.Marker([-2.902756, 104.688294], popup='Lorong Bersama').add_to(map_1)
folium.Marker([-2.903451, 104.698308], popup='Almi Caterindo').add_to(map_1)
folium.Marker([-2.922394, 104.754035], popup='Sukajaya').add_to(map_1)
folium.Marker([-2.938852, 104.710090], popup='Karya Baru').add_to(map_1)
folium.Marker([-2.873721, 104.697151], popup='SMP Negeri 49').add_to(map_1)
folium.Marker([-2.894901, 104.704736], popup='Bandara Sultan Mahmud Badaruddin').add_to(map_1)
folium.Marker([-3.025091, 104.807969], popup='Toko Elli').add_to(map_1)
folium.Marker([-3.025814, 104.808892], popup='Talang petai').add_to(map_1)
folium.Marker([-3.023784, 104.792690], popup='Kantin Ersya').add_to(map_1)
folium.Marker([-3.021470, 104.792969], popup='Stadion Atletic Jakabaring').add_to(map_1)
folium.Marker([-3.027973, 104.788431], popup='Warung Nando').add_to(map_1)
folium.Marker([-3.029993, 104.787771], popup='Bakso Aby').add_to(map_1)
folium.Marker([-3.029323, 104.788940], popup='Warung Nenekku').add_to(map_1)
folium.Marker([-3.034348, 104.793570], popup='Fersara Gym').add_to(map_1)
folium.Marker([-3.051185, 104.790705], popup='Wrp pesisir raya').add_to(map_1)
folium.Marker([-3.049262, 104.791687], popup='Toko Mila').add_to(map_1)
folium.Marker([-2.978126, 104.738268], popup='Rumah Makan Podomoro').add_to(map_1)
folium.Marker([-2.979026, 104.737640], popup='Emeral Perdana Abadi').add_to(map_1)
folium.Marker([-2.980001, 104.737458], popup='AW').add_to(map_1)
folium.Marker([-2.983488, 104.737297], popup='Vihara Hok Sin Tong').add_to(map_1)
folium.Marker([-2.984565, 104.737410], popup='Greatmixing DJ School').add_to(map_1)
folium.Marker([-2.985347, 104.737410], popup='TPU Puncak Sekuning').add_to(map_1)
folium.Marker([-2.986301, 104.740500], popup='Radio Singa Mania FM').add_to(map_1)
folium.Marker([-2.989076, 104.738847], popup='Refleksi Tradisional Bina Sehat 1').add_to(map_1)
folium.Marker([-2.988816, 104.742547], popup='Telaga Park').add_to(map_1)
folium.Marker([-2.991736, 104.734817], popup='Mie Pangsit Aang').add_to(map_1)
folium.Marker([-2.991414, 104.731813], popup='Pondok Abiqu').add_to(map_1)
folium.Marker([-3.013807, 104.794653], popup='Taman Danau').add_to(map_1)
folium.Marker([-3.035439, 104.792129], popup='Opi Regency').add_to(map_1)
folium.Marker([-3.036103, 104.791667], popup='Amanda Colection').add_to(map_1)
folium.Marker([-3.047002, 104.791110], popup='Sma negri 19 palembang').add_to(map_1)
folium.Marker([-3.050882, 104.788439], popup='Wira kost').add_to(map_1)
folium.Marker([-3.051503, 104.785670], popup='Cathering Ibu Sri').add_to(map_1)
folium.Marker([-3.050880, 104.785564], popup='HFC').add_to(map_1)
folium.Marker([-3.050634, 104.785229], popup='Bakery Azzura').add_to(map_1)
folium.Marker([-3.050827, 104.784715], popup='Spyro').add_to(map_1)
folium.Marker([-3.050119, 104.784706], popup='Arvi Aluminium').add_to(map_1)
folium.Marker([-2.932339, 104.785294], popup= 'Bakso Malang Merdeka').add_to(map_1)
folium.Marker([-2.932209, 104.784201], popup= 'Bunda Darell').add_to(map_1)
folium.Marker([-2.932055, 104.784068], popup= 'BFC Cafe').add_to(map_1)
folium.Marker([-2.932239, 104.785154], popup= 'Warung Kelvin').add_to(map_1)
folium.Marker([-2.932219, 104.784372], popup= 'BENGKEL BERKAT MOTOR').add_to(map_1)
folium.Marker([-2.932283, 104.785417], popup= 'Pangkas Rambut Singgalang').add_to(map_1)
folium.Marker([-2.932352, 104.785541], popup= 'Pempek Mancek Musi Raya Timur').add_to(map_1)
folium.Marker([-2.932077, 104.785981], popup= 'Viva Dangdut Group').add_to(map_1)
folium.Marker([-2.931975, 104.785606], popup= 'Viavasa').add_to(map_1)
folium.Marker([-2.931850, 104.785808], popup= 'Meegoesgallery').add_to(map_1)
folium.Marker([-3.007282, 104.807210], popup= 'Kelurahan Talang Bubuk').add_to(map_1)
folium.Marker([-3.007201, 104.809538], popup= 'Masjid Darussalam').add_to(map_1)
folium.Marker([-3.004394, 104.809927], popup= 'Koko Al').add_to(map_1)
folium.Marker([-3.004249, 104.807476], popup= 'SMP Negeri 20 Palembang').add_to(map_1)
folium.Marker([-3.004217, 104.808109], popup= 'SMAN 4 Palembang').add_to(map_1)
folium.Marker([-3.004887, 104.807825], popup= 'Rumah Makan Martabak India').add_to(map_1)
folium.Marker([-3.003489, 104.808430], popup= 'Masjid Salsabila').add_to(map_1)
folium.Marker([-3.002118, 104.808323], popup= 'Toko Kelontong Patimah').add_to(map_1)
folium.Marker([-3.000473, 104.805855], popup= 'Home_Boerger.id').add_to(map_1)
folium.Marker([-3.000762, 104.804235], popup= 'Masjid Al-Mustaqim').add_to(map_1)
folium.Marker([-2.902412, 104.699584], popup='Stasiun Meteorologi').add_to(map_1)
folium.Marker([-2.903208, 104.699862], popup='Federasi Aero Indonesia').add_to(map_1)
folium.Marker([-2.903167, 104.699512], popup='Pangkalan TNI AU Mess Perwira Satyo').add_to(map_1)
folium.Marker([-2.905729, 104.698352], popup='Warung Kabul').add_to(map_1)
folium.Marker([-2.906912, 104.696497], popup='Warung Ibu Lia').add_to(map_1)
folium.Marker([-2.907231, 104.696415], popup='Warung Bukde').add_to(map_1)
folium.Marker([-2.907438, 104.696216], popup='Warung Martini').add_to(map_1)
folium.Marker([-2.907451, 104.696972], popup='Amelia Shop Parfums').add_to(map_1)
folium.Marker([-2.907145, 104.696216], popup='Deko Argo Mandiri').add_to(map_1)
folium.Marker([-2.907111, 104.696644], popup='Toko Hikari').add_to(map_1)
folium.Marker([-2.986427, 104.726620], popup='Lapangan Pelita').add_to(map_1)
folium.Marker([-2.985115, 104.726588], popup='Pempek Naila').add_to(map_1)
folium.Marker([-2.984199, 104.728235], popup='Harapan Mulya').add_to(map_1)
folium.Marker([-2.988265, 104.729613], popup='Pahala Kencana').add_to(map_1)
folium.Marker([-2.993510, 104.729967], popup='STIE APRIN').add_to(map_1)
folium.Marker([-2.996054, 104.732639], popup='Masjid Baiturrahman').add_to(map_1)
folium.Marker([-2.998805, 104.735157], popup='Kelenteng Lam San Keng').add_to(map_1)
folium.Marker([-2.980093, 104.731624], popup='Sekolah Menengah Atas R.A Kartini Palembang').add_to(map_1)
folium.Marker([-2.977516, 104.732756], popup='Ellen Kost').add_to(map_1)
folium.Marker([-2.971152, 104.730143], popup='Restoran Indah Raso').add_to(map_1)
folium.Marker([-3.024909, 104.759185], popup='Ogan Baru').add_to(map_1)
folium.Marker([-3.034508, 104.761588], popup='Kemas Rindo').add_to(map_1)
folium.Marker([-3.029559, 104.781748], popup='Makin Jaya Toko').add_to(map_1)
folium.Marker([-3.014995, 104.779529], popup='Pondok Har Har').add_to(map_1)
folium.Marker([-3.016025, 104.779516], popup='Depot Kayu Raja').add_to(map_1)
folium.Marker([-3.016916, 104.780081], popup='Pondok Ibu Kito').add_to(map_1)
folium.Marker([-3.018550, 104.781213], popup='A dan A Cell').add_to(map_1)
folium.Marker([-3.019759, 104.781980], popup='Bengkel Mobil Fikri').add_to(map_1)
folium.Marker([-3.020135, 104.782377], popup='Toko Brama').add_to(map_1)
folium.Marker([-3.020444, 104.782397], popup='Ardaza').add_to(map_1)
folium.Marker([-2.880762, 104.703659], popup='Pesantren Zaadul Maad').add_to(map_1)
folium.Marker([-2.883550, 104.703829], popup='Toko Siti Digital 2 (cannon)').add_to(map_1)
folium.Marker([-2.884353, 104.705066], popup='Bengkel Las Sriwijaya').add_to(map_1)
folium.Marker([-2.884375, 104.705088], popup='Toko Besi dan Bahan Sriwijaya').add_to(map_1)
folium.Marker([-2.885058, 104.703484], popup='Depot Air Minum Arinda').add_to(map_1)
folium.Marker([-2.884086, 104.701634], popup='Masjid Miftahul Anwar').add_to(map_1)
folium.Marker([-2.883036, 104.700241], popup='Sate Padang Uni Yen').add_to(map_1)
folium.Marker([-2.883745, 104.699899], popup='Buah Segar Yahya').add_to(map_1)
folium.Marker([-3.005743, 104.818049], popup='Rumah Sakit Ibu Dan Anak Marissa').add_to(map_1)
folium.Marker([-3.011374, 104.820264], popup='Rumah Makan Budi Mulya').add_to(map_1)
folium.Marker([-3.017137, 104.826468], popup='Depot Kayu Zahara Jaya').add_to(map_1)
folium.Marker([-3.018964, 104.827954], popup='TiKi Gerai Sungai Pinang').add_to(map_1)
folium.Marker([-3.019478, 104.830572], popup='Masjid Pajrul Iman').add_to(map_1)
folium.Marker([-3.018471, 104.832605], popup='Musholla NURUL HIDAYAH').add_to(map_1)
folium.Marker([-3.022564, 104.834182], popup='TANGSIS 77 (KENTANG SOSIS)').add_to(map_1)
folium.Marker([-3.024153, 104.832388], popup='Bengkel Thoriq').add_to(map_1)
folium.Marker([-3.029768, 104.832593], popup='SMP Putra Maju Sungai Pinang').add_to(map_1)
folium.Marker([-3.030701, 104.835726], popup='Pelabuhan Goro RR').add_to(map_1)
folium.Marker([-2.931369, 104.785304], popup= 'Taman Pendidikan Al-Quran (TPA/TPQ)').add_to(map_1)
folium.Marker([-2.931340, 104.785612], popup= 'warung bu may').add_to(map_1)
folium.Marker([-2.930529, 104.784768], popup= 'Sekolah Dasar Negeri 118 Palembang').add_to(map_1)
folium.Marker([-2.930152, 104.785759], popup= 'Masjid Al Falah').add_to(map_1)
folium.Marker([-2.930389, 104.786303], popup= 'Pendekar Ilusi').add_to(map_1)
folium.Marker([-2.930094, 104.786577], popup= 'Komplek Griya Musi Permai').add_to(map_1)
folium.Marker([-2.930150, 104.785749], popup= 'Masjid Al Falah').add_to(map_1)
folium.Marker([-2.931559, 104.783898], popup= 'rumah cafe bu wahab').add_to(map_1)
folium.Marker([-2.931600, 104.783603], popup= 'Mitra Kreasi').add_to(map_1)
folium.Marker([-2.931479, 104.783665], popup= 'Milan Ac').add_to(map_1)
folium.Marker([-2.969409, 104.725865], popup= 'Grand Atyasa Convention Center').add_to(map_1)
folium.Marker([-2.966452, 104.727174], popup= 'Babyshop Palembang').add_to(map_1)
folium.Marker([-2.962316, 104.719986], popup= 'Pakjo Motor').add_to(map_1)
folium.Marker([-2.960634, 104.721284], popup= 'Bengkel Las Anugrah Sentosa').add_to(map_1)
folium.Marker([-2.960763, 104.723655], popup= 'Lapas Khusus Anak Palembang').add_to(map_1)
folium.Marker([-2.967770, 104.733955], popup= 'Rumah Limas').add_to(map_1)
folium.Marker([-2.969859, 104.713237], popup= 'PT. Swarna Cinde Raya').add_to(map_1)
folium.Marker([-2.971006, 104.712518], popup= 'PT. Intraco Penta Tbk').add_to(map_1)
folium.Marker([-2.975849, 104.723580], popup= 'Balai Diklat Keagamaan').add_to(map_1)
folium.Marker([-2.974167, 104.726541], popup= 'Rumah Makan Sederhana').add_to(map_1)
folium.Marker([-2.884041, 104.696551], popup='Masjid Jami Al-Jihad').add_to(map_1)
folium.Marker([-2.879540, 104.680057], popup='Deninteldan II/SWJ').add_to(map_1)
folium.Marker([-2.882488, 104.682333], popup='Depi Sano.CV').add_to(map_1)
folium.Marker([-2.881910, 104.682947], popup='BC HNI Palembang 3').add_to(map_1)
folium.Marker([-2.886376, 104.680278], popup='Salma Park Residence').add_to(map_1)
folium.Marker([-2.885274, 104.687953], popup='Model Sumiah').add_to(map_1)
folium.Marker([-3.024596, 104.783775], popup='Pindang Meranjat').add_to(map_1)
folium.Marker([-3.023511, 104.781186], popup='PT Golden Hikari').add_to(map_1)
folium.Marker([-3.034747, 104.782923], popup='Yayan Resto').add_to(map_1)
folium.Marker([-3.043612, 104.784715], popup='Klinik Kecantikan').add_to(map_1)
folium.Marker([-3.044609, 104.784794], popup='Jenica Salon').add_to(map_1)
folium.Marker([-3.046045, 104.784505], popup='Sinar Motor').add_to(map_1)
folium.Marker([-3.051952, 104.784525], popup='Toko Plastik').add_to(map_1)
folium.Marker([-3.048831, 104.790789], popup='SD Negeri 81 PLG').add_to(map_1)
folium.Marker([-3.049356, 104.788241], popup='Alfamart opi raya 2').add_to(map_1)
folium.Marker([-3.046930, 104.793744], popup='Kolam Pemancingan Alam').add_to(map_1)
folium.Marker([-2.930726, 104.782718], popup= 'Yayasan Islam Akbar').add_to(map_1)
folium.Marker([-2.930925, 104.783126], popup= 'JAHITAN UNI MAMA').add_to(map_1)
folium.Marker([-2.931206, 104.782927], popup= 'RPM Sako').add_to(map_1)
folium.Marker([-2.989961, 104.759967], popup= 'Benteng Kuto Besak').add_to(map_1)
folium.Marker([-2.976174, 104.753586], popup= 'Rk Charitas').add_to(map_1)
folium.Marker([-2.975558, 104.754466], popup= 'Kantor Perwakilan Bank Indonesia Provinsi Sumatera Selatan').add_to(map_1)
folium.Marker([-2.970104, 104.750142], popup= 'Markas Kodam II Sriwijaya').add_to(map_1)
folium.Marker([-2.961108, 104.739859], popup= 'KANTOR POLDA SUMATERA SELATAN').add_to(map_1)
folium.Marker([-2.887532, 104.689052], popup='Duta Mandiri Motor').add_to(map_1)
folium.Marker([-2.888039, 104.688600], popup='Apotek Bersama 2').add_to(map_1)
folium.Marker([-2.888279, 104.688318], popup='Nasi Goreng Kopral Dedy').add_to(map_1)
folium.Marker([-2.888146, 104.687953], popup='Griya Duta Lestari').add_to(map_1)
folium.Marker([-2.891613, 104.697712], popup='Ronny Cafe').add_to(map_1)
folium.Marker([-2.908609, 104.713773], popup='Masjid Babussalam').add_to(map_1)



folium.RegularPolygonMarker(
    [-3.011381, 104.820301],
    popup='Rumah Makan Budi Mulya',
    fill_color='#132b5e',
    number_of_sides=3,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.020916, 104.808284],
    popup='Sports Complex',
    fill_color='#45647d',
    number_of_sides=4,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.256144, 104.646985],
    popup='RSUD Kabupaten Ogan Ilir',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.192116, 104.744920],
    popup='SMAN 1 Pemulutan Barat',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.111450, 104.761933],
    popup='Warung Evang',
    fill_color='#132b5e',
    number_of_sides=3,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.097138, 104.793004],
    popup='Majelis Talim Nurul Kawakib',
    fill_color='#45647d',
    number_of_sides=4,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.084710, 104.813345],
    popup='Masjid Al-Khoiriyah',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.908601, 104.714681],
    popup='GARAGES99',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.910807, 104.714196],
    popup='SUKRO',
    fill_color='#769d96',
    number_of_sides=6,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.911560, 104.713296],
    popup='Lamun Ombak Cabang Padang',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.911898, 104.713108],
    popup='Kaos Wong Kito',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.030952, 104.798970],
    popup='Multipurpose Building Palmera',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.059925, 104.817622],
    popup='Meritai Anggrek Indah',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-3.062753, 104.818716],
    popup='Home Goods Store',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.987786, 104.760178],
    popup='Masjid Agung Palembang',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.983711, 104.757764],
    popup='Internasiona Plaza',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.984983, 104.753653],
    popup='Palembang Indah Mall',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.975945, 104.741647],
    popup='Palembang Square Mall',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.975945, 104.741647],
    popup='Palembang Square Mall',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.976042, 104.738343],
    popup='TVRI Sumatera Selatan',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.973567, 104.731659],
    popup='Dinas Kebudayaan dan Pariwisata Provinsi Sumatera Selatan',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-20964781, 104.720233],
    popup='Seblak Nampol',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.931238, 104.781820],
    popup='Martabak "Telor DOA IBU"',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
folium.RegularPolygonMarker(
    [-2.931131, 104.781986],
    popup='Dyska hijab palembang',
    fill_color='#769d96',
    number_of_sides=8,
    radius=10
    ).add_to(map_1)
map_1

	
folium.Circle(
    radius=100,
    location=[-2.930442, 104.782428],
    popup='Seblak & Jasuke Mak Mega',
    color='blue',
    fill=False,
).add_to(c)
c

folium.Marker(
    location=[-2.930646, 104.783155],
    popup='Ayumi Petshop',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.931187, 104.783700],
    popup='BAKSO DADI MULYO PERUMNAS',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.931490, 104.783735],
    popup='Apotek Sultan',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.930801, 104.783346],
    popup='Western Union',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.884774, 104.698883],
    popup='Masjid Komp Dirgantara Permai BTN',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.881502, 104.701310],
    popup='Darussofa Palembang',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.882502, 104.700320],
    popup='Mushala Masjid Lama',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.882186, 104.698873],
    popup='RSH Griya Marga Jaya',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.990158, 104.763337],
    popup='Wisata Kuliner Tepian Sungai Musi',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.985658, 104.767092],
    popup='PT. Indoforma Global Medika',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.979127, 104.764941],
    popup='V-Gen Mobile Servis Center',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.979931, 104.764834],
    popup='Evo Pet Shop Dempo - Palembang',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.975634, 104.766647],
    popup='CGV',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.974424, 104.765263],
    popup='Rajawali Grand Ballroom',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.970995, 104.764651],
    popup='Grand Zuri Hotel',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.969013, 104.763621],
    popup='RSIA Tiara Fatrin',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.966559, 104.765789],
    popup='Catholic University Musi-Caritas',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.967320, 104.764249],
    popup='SMA Xaverius 1',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.881205, 104.703606],
    popup='Masjid Sulaiman Al-Quraida',
    icon=folium.Icon(icon='cloud')
).add_to(d)
folium.Marker(
    location=[-2.882642, 104.703353],
    popup='Farhan Kreasi Palembang',
    icon=folium.Icon(icon='cloud')
).add_to(d)
d


simpan(map_1,'4.html')
simpan(c,'5.html')
simpan(d,'6.html')
