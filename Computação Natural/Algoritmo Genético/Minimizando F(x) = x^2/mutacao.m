function POPnovo = mutacao(POP,xmin,xmax,metMUT)
    % Apenas para auxílio, caso necessário
    [tamPOP, numVAR] = size(POP);

    switch metMUT
        case 1 % valor aleatório até 50% do espaço de busca
            POPnovo = (rand - .5) * (xmax - xmin);
        case 2 % valor aleatório até 50% do valor de C
            C = 0.2; % altere o valor de C
            POPnovo = (rand - .5) * C;
        case 3 % valor aleatório
            POPnovo =  rand * (xmax - xmin);
        otherwise
            fprintf('MÉTODO DE CRUZAMENTO NÃO IMPLEMENTADO');
    end
    
    % Para garantir que a nova população não extrapole o espaco de busca
    POPnovo = max(POPnovo,xmin);
    POPnovo = min(POPnovo,xmax);    
end