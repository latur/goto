//  Created by Stepan on 20/07/16.

import Foundation

class FrequensyAnalysisTester {
    static func test (data: [String: [String]]) -> String {
        let freqs: [String : [String: Int]] = ["C":["H":149970,"Q":200885,"V":273681,"D":134433,".":306363,"L":549431,"W":69816,"I":414598,
                                                    "K":457039,"F":511057,"M":89826,"S":489732,"A":187539,"T":273618,"N":315976,"C":160347,
                                                    "Y":177681,"R":323366,"G":189036,"P":189055,"E":216931],
                                               "E":["H":132591,"Q":181320,"V":248470,"D":130566,".":278294,"L":512086,"W":69184,"K":459305,
                                                    "M":76313,"I":376792,"F":510160,"S":458255,"A":217490,"N":296013,"C":142791,"T":248404,
                                                    "Y":142365,"R":365283,"G":217074,"P":217042,"E":205258]]
        var result = ""
    
            for read in data["X"]! {
                let testFreq = FrequencyCalculator.calculate(read)
                let cDistance = euclidianDistance(testFreq, second: freqs["C"]!)
                let eDistance = euclidianDistance(testFreq, second: freqs["E"]!)
                
                if cDistance < eDistance {
                    result += "C "
                }
                else {
                    result += "E "
                }
            }
        return result
    }
    
    private static func euclidianDistance (first: [String: Int], second: [String: Int]) -> Int {
        var first = first
        var second = second
        normalize(&first)
        normalize(&second)
        
        var distance: Int = 0
        for (key, value) in first {
            distance += (value-second[key]!)*(value-second[key]!)
        }
        
        return distance
    }
    
    private static func normalize (inout vector: [String: Int]) {
        var sum: Int = 0
        for (_, value) in vector {
            sum += value
        }
        for (key, value) in vector {
            vector[key]! = Int(Float(value)/Float(sum)*100)
        }
    }
}
