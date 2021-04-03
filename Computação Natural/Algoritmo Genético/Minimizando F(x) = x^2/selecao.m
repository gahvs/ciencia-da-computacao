function [POP, FX] = selecao(POP,FX,tamPOP,metSEL)
    
    switch metSEL
        case 1
            [POP, FX] = selecaosimples(POP,FX,tamPOP);
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