class Solution {
    func asteroidsDestroyed(_ mass: Int, _ asteroids: [Int]) -> Bool {
        let sortedAsteroids = asteroids.sorted()
        var mass = mass
        
        for asteroid in sortedAsteroids {
            if mass < asteroid { return false }
            else {
                mass += asteroid
            }
        }
        
        return true
    }
}
