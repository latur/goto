//  Created by Stepan on 19/07/16.

import Foundation

class FrequencyAnalysisTrainer {
    static func train (parsedData: [String: [String]]) -> NSData {
        var proteinFrequencies: [String: [String: Int]] = ["E": [:], "C": [:]]
        addFrequenciesForType(parsedData, typeName: "E", proteinFrequencies: &proteinFrequencies["E"]!)
        addFrequenciesForType(parsedData, typeName: "C", proteinFrequencies: &proteinFrequencies["C"]!)
        
        //JSON creation
        guard let json = try? NSJSONSerialization.dataWithJSONObject(proteinFrequencies, options: []) else {
            print ("NSJSONSer Error")
            exit(228)
        }
        
        return json
    }
    
    private static func addFrequenciesForType (parsedData: [String: [String]], typeName: String, inout proteinFrequencies: [String: Int]) {
        guard parsedData[typeName] != nil else {
            print ("invalid typeName")
            exit(228)
        }

        for read in parsedData[typeName]! {
            let frequencies = FrequencyCalculator.calculate(read)
            
            for (key, value) in frequencies {
                if proteinFrequencies[key] == nil {
                   proteinFrequencies[key] = value
                }
                else {
                    proteinFrequencies[key]! += value
                }
            }
        }
        //TODO:  дописать код!
//        for (key, value) in proteinFrequencies {
//            let readsCount = parsedData[typeName]!.count
//            print(proteinFrequencies[key]!)
//            proteinFrequencies[key]! = value/readsCount
//            print(proteinFrequencies[key]!)
//
//        }
    }
}
