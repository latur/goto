//  Created by Stepan on 19/07/16.

import Foundation

class GCContentTester {
    static func test (data: [String: [String]]) -> String {
        var result = ""
        
        for read in data["X"]! {
            var GCC: Float = 0
            GCC = GCContentCalc.calculate(read)*100
            if  GCC >= 33.0 && GCC <= 40.0 {
                result += "E "
            }
            else {
                result += "C "
            }
        }
        return result
    }
}