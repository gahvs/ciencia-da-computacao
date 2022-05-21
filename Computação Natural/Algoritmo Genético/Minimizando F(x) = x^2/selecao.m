function [POP, FX] = selecao(POP,FX,tamPOP,metSEL)
    
    switch metSEL
        case 1
            [POP, FX] = selecaosimples(POP,FX,tamPOP);
        case 2
            [POP, FX] = selecaoPorTorneio(POP, FX, 2, tamPOP);
    end
end

function [POP, FX] = selecaosimples(POP,FX,tamPOP)
    % Ordena a população do menor (melhor) para o maior
    [~, ind] = sort(FX);
    
    % Reduz o tamanho de ind para o valor desejado (tamPOP)
    ind = ind(1:tamPOP);
    
    % Atualiza a população, com apenas os tamPOP melhores indivíduos
    POP = POP(ind,:);
    FX = FX(ind,:);
end

function [POP, FX] = selecaoPorTorneio(POP, FX, slice, tamPOP)

    newPOP = [];
    
    for z = 1:tamPOP
        
        for t = 1:slice
            ind1 = POP(randsample(10, 1));
            ind2 = POP(randsample(10, 1));
            
            if calculafx(ind1, 1) > calculafx(ind2, 1)
                newPOP(end+1) = ind1;
            elseif
                newPOP(end+1) = ind2;
            end
            
        end
    
    end
    POP = newPOP
    FX = calculafx(newPOP, 1)
end

function [POP, FX] = selecaoPorRoleta(POP, FX , tamPOP)

end