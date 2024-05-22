class Airline:
    def __init__(self):
        self.plane_list = []
        self.route_list = []

    def add_plane(self, plane):
        self.plane_list.append(plane)
        print('Самолет добавлен в список самолетов')

    def remove_plane(self, plane):
        if plane in self.plane_list:
            self.plane_list.remove(plane)
            print('Самолет удален из списка самолетов')

    def add_route(self, route):
        self.route_list.append(route)
        print('Маршрут добавлен в список маршрутов')

    def remove_route(self, route):
        if route in self.route_list:
            self.route_list.remove(route)
            print('Маршрут удален из списка маршрутов')

    def find_plane(self, model):
        for plane in self.plane_list:
            if plane == model:
                return 'Самолет найден в списке самолетов.'
        return 'Самолет не найден в списке самолетов.'

    def find_route(self, city):
        available_routes = [route for route in self.route_list if city in route]
        return available_routes
