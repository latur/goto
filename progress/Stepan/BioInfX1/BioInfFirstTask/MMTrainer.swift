//  Created by Stepan on 20/07/16.

import Foundation

class MMTrainer {
    static func train (parsedData: [String: [String]], degree: Int) -> [String: [String: Float]] {
        var MMChain: [String: [String: Float]] = ["E": [:], "C": [:]]
        
        MMCalculator.calculate(parsedData["E"]!, chain: &MMChain["E"]!, degree: degree)
        MMCalculator.calculate(parsedData["C"]!, chain: &MMChain["C"]!, degree: degree)
        
//        //JSON creation
//        guard let json = try? NSJSONSerialization.dataWithJSONObject(MMChain, options: []) else {
//            print ("NSJSONSer Error")
//            exit(228)
//        }
//        
//        return json
        
        return MMChain
    }
}