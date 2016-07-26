//  Created by Stepan on 19/07/16.

import Foundation

class FrequencyCalculator {
    
    static func calculate (read: String) -> [String: Int] {
        var result: [String: Int] = [:]
        
        writeProteinCount(read, result: &result)
        
        let transposedRead = transpose(read)
        
        writeProteinCount (transposedRead, result: &result)
        
        //FIXME: погрешность большая
        //  усреднение значений из-за шести проходов
//        for (key, value) in result {
//            result[key] = value/6
//        }
        
        return result
    }
    
    static private func writeProteinCount (read: String, inout result: [String: Int]) {
        let proteins: [String: String] = ["AAA":"K", "AAC":"N", "AAG":"K", "AAT":"N", "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
                                          "AGA":"R", "AGC":"S", "AGG":"R", "AGT":"S", "ATA":"I", "ATC":"I", "ATG":"M", "ATT":"I",
                                          "CAA":"Q", "CAC":"H", "CAG":"Q", "CAT":"H", "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
                                          "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R", "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
                                          "GAA":"E", "GAC":"D", "GAG":"E", "GAT":"D", "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
                                          "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G", "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
                                          "TAA":".", "TAC":"Y", "TAG":".", "TAT":"Y", "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
                                          "TGA":".", "TGC":"C", "TGG":"W", "TGT":"C", "TTA":"L", "TTC":"F", "TTG":"L", "TTT":"F"]
        
        var first  = read[read.startIndex]
        var second = read[read.startIndex.successor()]
        var third  = read[read.startIndex.successor().successor()] //можно и по-другому, но и так норм пожалуй
        
        for character in read.characters.dropFirst(3) {
            let proteinCode = String(first)+String(second)+String(third)
            guard let protein = proteins[proteinCode] else {
                print ("  no such proteinCode in table")
                exit(228)
            }
            if result[protein] == nil {
                result[protein] = 1
            }
            else {
                result[protein]! += 1
            }
            
            first = second
            second = third
            third = character
        }
    }

    static private func transpose (read: String) -> String {
        //A->T, G->C
        let changeTable: [String: String] = ["A": "T", "T": "A", "G": "C", "C": "G"]
        
        var transposed = ""
        
        for character in read.characters.reverse() {
            guard let changedCharacter = changeTable[String(character)] else {
                print ("unknown character")
                exit(228)
            }
            transposed += changedCharacter
        }
        return transposed
    }
}
