//  Created by Stepan on 23/07/16.

import Foundation

typealias dependency = (gene1: String, gene2: String, multiplier: Float)

class GeneGraph {
    private let edges: [String: [String: Float]]
    private var expressions: [String: Float]
    
    init (dependencies: [dependency], defaultExpresions: [String: Float]) {
        var tempEdges = [String: [String: Float]]()
        for value in dependencies {
            if tempEdges[value.gene1] == nil {
                tempEdges[value.gene1] = [:]
            }
            tempEdges[value.gene1]![value.gene2] = value.multiplier
        }
        edges = tempEdges
        expressions = defaultExpresions
    }
    
    func getDependencyFromGene(gene1: String, )
}
