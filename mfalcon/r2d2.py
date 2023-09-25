import sqlite3


class R2D2(object):
    """
    R2D2 compiles all the information from the Millenium Falcon's congif file 
    and Empire's leak files and computes the odds of survival.
    """

    def __init__(self, falcon_config, empire_leaks):
        # Initialize R2D2
        self.db = falcon_config['routes_db']
        self.routes = self.get_routes(self.db)
        self.autonomy = falcon_config['autonomy']
        self.departure = falcon_config['departure']
        self.arrival = falcon_config['arrival']
        self.countdown = empire_leaks['countdown']
        self.bounty_hunters = {}
        for e in empire_leaks['bounty_hunters']:
            if e['planet'] in self.bounty_hunters:
                self.bounty_hunters[e['planet']] += [e['day']]
            else:
                self.bounty_hunters[e['planet']] = [e['day']]


    def get_routes(self, db):
        # Get routes from database
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute("SELECT * FROM routes")
        rows = cur.fetchall()
        return rows
    

    def possible_routes(self):
        """
        Compute all possible routes and return the safest ones.
        The algorithm is a greedy recursive function that explores all possible routes.

        """
        def possible_routes_rec(journey, countdown, fuel, hunters):
            """
            Recursive function that records:
                - the current *journey*
                - the current *countdown*
                - current *fuel* (autonomy left)
                - current number of bounty *hunters* crossed
            """
            # If we reached the destination, return the journey.
            if journey[-1][0] == self.arrival:
                return [(journey, hunters)]
            # If the countdown is over, return None.
            if countdown == 0:
                return None
            
            # List all possible routes from current planet, with or without refuel.
            possible_routes_now = []
            possible_routes_refuel = []
            for r in self.routes:
                if r[0] == journey[-1][0] or r[1] == journey[-1][0]:
                        if r[2] <= fuel and r[2] <= countdown: 
                            # possible routes without refuel
                            if r[0] == journey[-1][0]:
                                possible_routes_now.append((r[1],r[2]))
                            else:
                                possible_routes_now.append((r[0],r[2]))
                        elif r[2] <= self.autonomy and r[2] <= countdown - 1:
                            # possible routes with refuel
                            if r[0] == journey[-1][0]:
                                possible_routes_refuel.append((r[1],r[2]))
                            else:
                                possible_routes_refuel.append((r[0],r[2]))
            results = []
            
            # Recursive search for the --no refuel-- option.
            for r in possible_routes_now:
                p = possible_routes_rec(journey+[(r[0], '')], countdown-r[1], fuel-r[1], \
                                        hunters + int(self.countdown - countdown in (self.bounty_hunters.get(journey[-1][0], []) or [])))
                if p:
                    results += p
            # Recursive search for the --refuel-- option.
            for r in possible_routes_refuel:
                p = possible_routes_rec(journey+[(journey[-1][0],' (refuel)'),(r[0],'')], countdown-1-r[1], self.autonomy-r[1],\
                                        hunters + 2*int(self.countdown - countdown in (self.bounty_hunters.get(journey[-1][0], []) or [])))
                if p:
                    results += p
            # Recursive search for the --stall-- option.
            p = possible_routes_rec(journey+[(journey[-1][0],' (stalling)')], countdown-1, fuel, \
                                    hunters + int(self.countdown - countdown in (self.bounty_hunters.get(journey[-1][0], []) or [])))
            if p:
                results += p
            # Choose the safest routes (e.g. with the least number of bounty hunters crossed).
            if results:
                safest = min([r[1] for r in results])
                res = [r for r in results if r[1] == safest]
                return res
            else:
                return None 
        return possible_routes_rec([(self.departure,' (Departure)')], self.countdown, self.autonomy, 0)


    def prob_func(self, k):
        # Mathematical formula to compute the odds of survival.
        return int((1-sum([9**j/(10**(j+1)) for j in range(k)]))*100)
    
    def get_odds(self):
        if self.possible_routes():
            return self.prob_func(self.possible_routes()[0][1])
        else:
            return 0

    def print_journeys(self):
        if self.possible_routes():
            for route in self.possible_routes():
                print('Odds are ' + str(self.prob_func(route[1])) + '% of survival.')
                print('Route: ' + ' - '.join([step[0] + step[1] for step in route[0]]))
        else:
            print('No possible route found.')

    def get_journey(self):
        return self.possible_routes()[0]
    
    def print_journey(self):
        if self.possible_routes():
            j = self.get_journey()
            print('Odds are ' + str(self.prob_func(j[1])) + '% of survival.')
            print('Route: ' + ' - '.join([step[0] + step[1] for step in j[0]]))
        else:
            print('No possible route found.')