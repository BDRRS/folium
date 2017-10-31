import folium
map_1 = folium.Map(location=[-2.9521793,104.7499501],
                   zoom_start=12,
                   tiles='Stamen Terrain')
folium.Marker([-2.952245, 104.758104], popup='pecel lele').add_to(map_1)
folium.Marker([-2.958722, 104.766448], popup='palembang golf club').add_to(map_1)
folium.Marker([-2.958754, 104.770375], popup='kopitiam').add_to(map_1)
folium.Marker([-2.958497, 104.770375], popup='the kitchen').add_to(map_1)
folium.Marker([-2.958379, 104.767178], popup='resto golf view').add_to(map_1)
folium.Marker([-2.962129, 104.769860], popup='baby store').add_to(map_1)
folium.Marker([-2.960500, 104.771502], popup='wisma grand kemala').add_to(map_1)
folium.Marker([-2.962225, 104.772950], popup='smp negeri 4 palembang').add_to(map_1)
folium.Marker([-2.962311, 104.773465], popup='smp negeri 50').add_to(map_1)
folium.Marker([-2.963350, 104.773240], popup='dexa medika').add_to(map_1)
map_1