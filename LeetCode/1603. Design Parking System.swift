class ParkingSystem {
    var states = Dictionary<Int,Int>()
    init(_ big: Int, _ medium: Int, _ small: Int) {
        self.states[1] = big; self.states[2] = medium; self.states[3] = small;
    }
    
    func addCar(_ carType: Int) -> Bool {
        if self.states[carType]! > 0{
            self.states[carType]! -= 1
            return true
        }
        return false
    }
}
